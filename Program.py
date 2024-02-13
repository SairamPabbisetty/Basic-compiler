import TokenGen
import re

while True :
    text = input(">")

    formatted_expression = re.sub(r'([+\-*/()])', r' \1 ', text)
    
    result, error = TokenGen.run("<stdin", formatted_expression)

    if error :
        print(error.as_string)
    else :
        print(result)