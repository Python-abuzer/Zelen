"Цена"
import pytest
from typing import Self
from src.сard import Card

class Price:
    VEGETABLES = Card.VEGETABLES
    MAX_PRICE = 5
    
    def __init__(self, **kwargs):
        for v in self.VEGETABLES:
            setattr(self, v, kwargs.get(v))
        self.d = kwargs.copy()
        self.validate_vegetables(kwargs.keys())
        self.validate_values()

    def validate_vegetables(self, symbols):
        if symbols not in self.VEGETABLES:
            raise ValueError
        
    def validate_values(self, **kwargs):
        if kwargs.values() not in range(6):
            raise ValueError
        
    def __repr__(self):
        return ''.join(list(f'{v}:{getattr(self, v)} ' for v in self.VEGETABLES))
    
    def __eq__(self, other):
       return self.t == other.t and self.b == other.b and self.c == other.c and self.e == other.e and self.cr == other.cr

    def add(self, other: str | dict | Self | Card):
        if isinstance(other, Price):
            other = other.d
        elif isinstance(other, dict):
            other = list(other.keys())
        elif isinstance(other, Card):
            other = list(str(other))
        elif isinstance(other, str):
            other = list(other)
        for v in other:
            if hasattr(self, v):
                setattr(self, v, (1 + getattr(self, v)) % (Price.MAX_PRICE + 1))
                self.d[v] = getattr(self, v)  
            else:
                print(f"Некорректный овощ: {v}") 



def test_init():
    p = Price(t=3, b=1, co=2, e=0, cr=4)
    assert p.t == 3
    assert p.b == 1
    assert p.co == 2
    assert p.e == 0
    assert p.cr != 3

def test_valid():
    with pytest.raises(ValueError):
        n = Price(t=52)

def test_save():
    p = Price(t=3, b=1, co=2, e=0, cr=4)
    assert repr(p) == 't:3 b:1 co:2 e:0 cr:4'

def test_add():
    v = Price(t=0, b=1, co=2, e=3, cr=4)
    v.add('tbb')
    assert v.t == 0
    assert v.b == 1
    assert v.co == 3
    assert v.e == 5