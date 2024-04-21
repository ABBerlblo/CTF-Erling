import random
# from InverseAlphabet import InverseAlphabet

def Salt():
    iteration = 0
    length = 12

    l = []
    while iteration < length: 
        char = chr(random.randint(65, 90))
        l.append(char if random.randint(0,1) == 1 else char.lower())
        # l.append(random.randint(1,56))
        iteration += 1  

    salt = ''.join(l)
    # salt = ''.join(map(str, l))

    return salt