
class Error :
    def __init__(self, pos_start, pos_end, error_name, details) -> None :
        self.pos_start = pos_start
        self.pos_end = pos_end 
        self.error_name = error_name
        self.details = details

    def as_string(self) :
        result = f'{self.error_name}: {self.details}'
        result += f'File{self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return "Error"

class IllegalCharError(Error) :
    def __init__(self, pos_start, pos_end, details) -> None :
        super().__init__(pos_start, pos_end, "Illegal Character", details)

class Position :
    def __init__(self, idx, ln, col, fname, ftext) -> None :
        self.idx = idx
        self.ln = ln
        self.col = col 
        self.fname = fname
        self.ftext = ftext
    
    def advance(self, current_char) :
        self.idx += 1
        self.col += 1

        if current_char == "\n" :
            self.ln += 1
            self.col += 1

        return self
    
    def copy(self) :
        return Position(self.idx, self.ln, self.col, self.ftext, self.fname)

DIGITS = '0123456789'

TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"

class Token :
    def __init__(self, type_, value=None) -> None :
        self.type = type_
        self.value = value 

    def __repr__(self) -> str :
        if self.value : 
            return f'{self.type}:{self.value}'
        return f'{self.type}'

class Lexer :
    def __init__(self, fname, text) -> None :
        self.fname = fname 
        self.text = text
        self.position = Position(-1, 0, -1, fname, text)
        self.current_char = None

        self.advance()

    def advance(self) :
        self.position.advance(self.current_char)
        if (self.position.idx < len(self.text)) :
            self.current_char = self.text[self.position.idx]
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
                pos_start = self.position.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.position, "'" + char + "'")

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
        
class NumberToken :
    def __init__(self, tok) -> None:
        self.tok = tok 
    
    def __repr__(self) -> str:
        return f'{self.tok}'
    
class BinOpNode :
    def __init__(self, left_node, op_tok, right_node) -> None:
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node
    
    def __repr__(self) -> str:
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'

def run(fname, text) :
    lexer = Lexer(fname, text)
    tokens, error = lexer.make_tokens()

    return tokens, error