"Цена"
class Price:
    def __init__(self,t=0,b=0,c=0,e=0):
        if 0 <= t <= 5:
            if 0 <= b <= 5:
                if 0 <= c <= 5:
                    if 0 <= e <= 5:
                        self.t = t
                        self.b = b
                        self.c = c
                        self.e = e
        else:
            raise ValueError
        
    def __repr__(self):
        return f'{self.t}{self.b}{self.c}{self.e}'
    
    def __eq__(self,other):
        if isinstance(other, str):
            return self.t == other.t and self.b == other.b and self.c == other.c and self.e == other.e
        
    def save(self):
        return repr(self)
    
    def add(price_str:str,card:str):
        price = Price.load(price_str)
        return f'{card}{price.save()}'