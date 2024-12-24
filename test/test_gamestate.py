import pytest

from src.сard import Card
from src.deck import Deck
from src.gamestate import GameState
from src.player import Player
from src.price import Price

data = {
        "Price": 't:2 b:1 c:4 e:0 a:0 ',
        "Deck": 'ttb tbb ttt ttb tbb bbb',
        "Round": 1,
        "CurrentPlayerIndex": 1,
        "cards": ['eee', 'cee', 'cce'],
        "players": [
            {'name': 'Player_1', 'hand': 'ttt bbb tbb', 'score': 6},
            {'name': 'Player_2', 'hand': 'ttb tbb ttb', 'score': 10}
                   ]
       }
Player_1 = Player.load(data["players"][0])
Player_2 = Player.load(data["players"][1])
cards = (Card.load(s) for s in data["cards"])
full_deck = Deck(None)
price = Price.load('t:2 b:1 c:4 e:0 a:0')
def test_init():
        players= [Player_1, Player_2]
        g = GameState(players=players, deck=full_deck, price=price, cards=cards, current_player=0, round_i=1)
        assert g.players == players
        assert g.deck == full_deck
        assert g.price == price
        assert g.cards == cards
        assert g._current_player == 0
        assert g.round_i == 1
    
def test_current_players():
    players = [Player_1, Player_2]
    g = GameState(players=players, deck=full_deck, price=price, cards=cards, round_i=1)
    assert g.current_player() == Player_1
    g = GameState(players=players, deck=full_deck, price=price, cards=cards, current_player=1, round_i=1)
    assert g.current_player() == Player_2

def test_eq():
    players = [Player_1, Player_2]
    g1 = GameState(players=players, deck=full_deck, price=price, cards=cards, round_i=1)
    g2 = GameState(players=players, deck=full_deck, price=price, cards=cards, round_i=1)
    assert g1 == g2
    g3 = GameState(players=players, deck=Deck(Card.all_cards(['e', 'a'])), price=price, cards=cards, round_i=2)
    assert g1 != g3

def test_save():
    players = [Player_1, Player_2]
    deck = Deck.load(data["Deck"])
    test_cards = [Card.load(s) for s in data["cards"]]
    test_price = Price.load(data["Price"])
    g = GameState(players=players, deck=deck, price=test_price, cards=test_cards, current_player = data["CurrentPlayerIndex"],round_i=data["Round"])
    assert g.save() == data

def test_load():
    g = GameState.load(data)
    assert g.save() == data

def test_next_player():
    g = GameState.load(data)
    assert str(g.current_player()) == 'Player_2(10):ttb tbb ttb'
    g.next_player()
    assert str(g.current_player()) == 'Player_1(6):ttt bbb tbb'
    g.next_player()
    assert str(g.current_player()) == 'Player_2(10):ttb tbb ttb'