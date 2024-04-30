import json, hashlib, random
from salty import Salt

def encrypt(message, salt):
    # Concatenate salt and message
    salted_message = salt + message

    # Hash the salted message using SHA-256
    hashed_message = hashlib.sha256(salted_message.encode()).hexdigest()

    return hashed_message

if __name__ == "__main__":
    # Read lines from information.txt and parse as JSON list
    information = json.load(open("./information2.txt", "r", encoding='UTF-8'))

    # Scramble the list
    random.shuffle(information)

    # Encrypt info
    encryption = {}
    for index, info in enumerate(information):
        salt = Salt(8)
        encrypted = encrypt(info, salt)

        encryption["user" + str(index + 1)] = [{"salt": salt, "info": encrypted}]

    # Write encryption dictionary to JSON file
    # json.dump(encryption, open("CTF-Uppgift 2/db.json", "w", encoding='UTF-8'))