from Decypher import Decypher

decryption = ''

secret = open("Output.txt", "r").read()

salt, message = secret[:12], secret[12:]
letters = [char for char in message]

decypher = ''.join(Decypher(letters, salt))
decryption += decypher

print(decryption)
