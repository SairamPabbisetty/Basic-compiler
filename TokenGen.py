from tokens import Float, Integer, Operator, Token

DIGITS = '0123456789'
OPERATORS = "+-*/()"

class Lexer :
    def __init__(self, fname, text) -> None :
        self.fname = fname 
        self.text = text
        self.idx = -1
        self.current_char = None

        self.advance()

    def advance(self) :
        self.idx += 1
        if (self.idx < len(self.text)) :
            self.current_char = self.text[self.idx]
        else :
            self.current_char = None 

    def make_tokens(self) :
        tokens = []
        token = self.current_char
        while self.current_char != None :
            if self.current_char in ' \t' :
                self.advance()
            elif self.current_char in DIGITS :
                tokens.append(self.make_number())
                self.advance()
            elif self.current_char in OPERATORS :
                tokens.append(Operator(self.current_char))
                self.advance()
            else :
                self.advance()
                return [], "IllegalCharError"

        return tokens, None

    def make_number(self) :
        number = ""
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.' :
            if self.current_char == '.' :
                if dot_count == 1 :
                    break
                dot_count = 1
                number += "."
            else :
                number += self.current_char
            self.advance()

        if dot_count == 0 :
            return Integer(int(number))
        else :
            return Float(float(number))

def run(fname, text) :
    lexer = Lexer(fname, text)
    tokens, error = lexer.make_tokens()

    return tokens, error