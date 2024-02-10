import TokenGen

while True :
    text = input(">")
    
    result, error = TokenGen.run(text)

    if error :
        print(error.as_string)
    else :
        print(result)