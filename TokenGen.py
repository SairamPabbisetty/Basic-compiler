
DIGITS = '0123456789'

TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_PLUS = "+"
TT_MINUS = "-"
TT_MUL = "*"
TT_DIV = "/"
TT_LPAREN = "("
TT_RPAREN = ")"

class Token :
    def __init__(self, type_, value=None) -> None :
        self.type = type_
        self.value = value 

    def __repr__(self) -> str :
        if self.value : 
            return f'{self.value}'
        return f'{self.type}'

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

        while self.current_char != None :
            if self.current_char in ' \t' :
                self.advance()
            elif self.current_char in DIGITS :
                tokens.append(self.make_number())
                self.advance()
            elif self.current_char == '+' :
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-' :
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*' :
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/' :
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(' :
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')' :
                tokens.append(Token(TT_RPAREN))
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
            return Token(TT_INT, int(number))
        else :
            return Token(TT_FLOAT, float(number))

def run(fname, text) :
    lexer = Lexer(fname, text)
    tokens, error = lexer.make_tokens()

    return tokens, error