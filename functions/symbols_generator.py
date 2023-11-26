def symbols_generator():
    letters = ""
    for i in range(97, 123):
        letters += chr(i)
    capital_letters = letters.upper()
    symbols =""
    for i in range(33, 65):
        symbols += chr(i)
    List = [letters, capital_letters, symbols]
    return List
