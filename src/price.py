"Цена"
from src.сard import Card
from typing import Self,Dict

class Price:
    VEGETABLES = Card.VEGETABLES
    MAX_PRICE = 5

    def __init__(self, **kwargs):
        self.d = {v: kwargs.get(v, 0) for v in self.VEGETABLES}  
        self.validate_vegetables(kwargs.keys())
        self.validate_values()

    def validate_vegetables(self, symbols):
        if not all(v in self.VEGETABLES for v in symbols):
            raise ValueError("Некорректные овощи")

    def validate_values(self):
        if not all(0 <= value <= self.MAX_PRICE for value in self.d.values()):
            raise ValueError("Некорректные значения цен")

    def __repr__(self):
        return ''.join(f'{v}:{self.d[v]} ' for v in self.VEGETABLES)
    
    def save(self):
        return repr(self)   
    
    def __eq__(self, other):
        if isinstance(other, Price):
            return self.d == other.d
        return False

    def add(self, other: Dict[str, int] | str | Card | Self):
        if isinstance(other, Price):
            other = other.d
        if isinstance(other, dict):
            for v in other:
                print(f"Add {v=} {self.d[v]=} {other[v]=}")
                if v in self.VEGETABLES:
                    self.d[v] = (self.d[v] + other[v]) % (Price.MAX_PRICE + 1)
                else:
                    print(f"Некорректный овощ: {v}")
            return
        
    @classmethod
    def load(cls, data: str):
        items = data.split()
        params = {item.split(':')[0]: int(item.split(':')[1]) for item in items}
        return cls(**params)
    
    def update_price(self, card: Card):
        card_value = card.save()
        for v in Card.VEGETABLES:
            count = card_value.count(v)
            setattr(self, v, getattr(self, v, 0) + count)