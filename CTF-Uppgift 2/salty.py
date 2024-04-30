import random

def Salt(length : int):
    iteration = 0

    salt = ""
    while iteration < length: 
        salt += str(random.randint(0,1))
        iteration += 1  

    return salt