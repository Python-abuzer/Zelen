
class Card:
    vegetables = ["t","b","c","e"]
    price = list(range(6))

    def __init__(self,vegs:str,pr:int):
        if vegs not in Card.vegetables:
            raise ValueError
        if pr not in Card.price:
            raise ValueError
        self.vegs = vegs
        self.pr = pr

    def __repr__(self):
        return f'{self.vegs}{self.pr}'
    
    def __eq__(self, other):
        if isinstance(other, str):
            other = Card.load(other)
        return self.vegs == other.vegs and self.pr == other.pr

    def save(self):
        return repr(self)    
    
    @staticmethod
    def load(text: str):
        return Card(vegs=text[0], pr=int(text[1]))