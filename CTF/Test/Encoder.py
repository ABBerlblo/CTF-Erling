from Cypher import Cypher
from SaltGenerator import Salt

encryption = ''

message = input()

letters = [char for char in message]

salt = Salt()
encryption += salt

cypher = ''.join(Cypher(letters, salt))
encryption += cypher

f = open("Output.txt", "w", encoding='UTF-8')
f.write(encryption)
f.close()