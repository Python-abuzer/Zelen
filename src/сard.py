"Карты"
class Card:
    vegetables = ["t","b","c","e"] #tomato,broccoli,corn,eggplant
    quantity = list(range(1,4))

    def __init__(self,vegs:str,quant:int):
        if vegs not in Card.vegetables:
            raise ValueError
        if quant not in Card.quantity:
            raise ValueError
        self.vegs = vegs
        self.quant = quant

    def __repr__(self):
        return f'{self.vegs}{self.quant}'
    
    def __eq__(self, other):
        if isinstance(other, str):
            other = Card.load(other)
        return self.vegs == other.vegs and self.quant == other.quant

    def save(self):
        return repr(self)    
    
    @staticmethod
    def load(text: str):
        return Card(vegs=text[0], quant=int(text[1]))