import re

import tokenGen
import parserGen
import interpreter

while True :
    text = input(">")

    formatted_expression = re.sub(r'([+\-*/()])', r' \1 ', text)
    
    tokens, error = tokenGen.run("<stdin>", formatted_expression)

    if error :
        print(error)
    else :
        print(tokens)
        parser = parserGen.Parser(tokens)
        tree = parser.parse()
        print(tree)
        interpret = interpreter.Interpreter(tree)
        result = interpret.interpret()
        print(result)