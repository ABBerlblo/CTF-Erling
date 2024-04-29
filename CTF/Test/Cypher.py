from Alphabet import Alphabet, InverseAlphabet, uniqueChars

def Cypher (letters : list, salt : str):
    cypher = []

    i = 1
    for preLetter in letters:
        value = 0
        value = Alphabet(preLetter)

        offset = 0
        for char in [char for char in salt]:
            offset += Alphabet(char)
        
        value += offset * i
        value %= uniqueChars
        
        postLetter = InverseAlphabet(value)
        cypher.append(postLetter)

        i += 1

    return cypher