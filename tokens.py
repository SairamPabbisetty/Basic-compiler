class Token :
    def __init__(self, type_, value=None) -> None :
        self.type = type_
        self.value = value 

    def __repr__(self) -> str :
        if self.value : 
            return f'{self.value}'
        return f'{self.type}'
    
class Integer(Token) :
    def __init__(self, value) :
        super().__init__("INT", value)

class Float(Token) :
    def __init__(self, value) :
        super().__init__("FLOAT", value)

class Operator(Token) :
    def __init__(self, value) :
        super().__init__("OPER", value)