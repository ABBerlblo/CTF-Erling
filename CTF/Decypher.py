from Alphabet import Alphabet, InverseAlphabet, uniqueChars

def Decypher (letters : list, salt : str):
    decypher = []

    i = 1
    for postLetter in letters:
        value = 0
        value = Alphabet(postLetter)

        offset = 0
        for char in [char for char in salt]:
            offset += Alphabet(char)

        value -= offset * i
        value %= uniqueChars

        print(value)
        
        preLetter = InverseAlphabet(value)
        decypher.append(preLetter)

        i += 1

    return decypher