import json, base64
from salty import Salt
from cryptography.fernet import Fernet

# Generate a random key for Fernet encryption
key = b'jZI7oc1mk4KXY1SA_Abg2kiLZey39jd8oATdw_CU_tE='
cipher = Fernet(key)

print(key)

def encrypt(message, salt):
    # Concatenate salt and message
    salted_message = salt + message

    # Encrypt the salted message using Fernet
    encrypted_message = cipher.encrypt(salted_message.encode())

    # Encode the encrypted message using base64 and convert to string
    encoded_encrypted_message = base64.urlsafe_b64encode(encrypted_message).decode()

    return encoded_encrypted_message

if __name__ == "__main__":
    # Read lines from information.txt and parse as JSON list
    information = json.load(open("./information.txt", "r", encoding='UTF-8'))

    # Encrypt info
    encryption = {}
    for index, info in enumerate(information):
        salt = Salt(8)
        encrypted = encrypt(info, salt)

        encryption["user" + str(index + 1)] = [{"salt": salt, "info": encrypted}]

    # Write encryption dictionary to JSON file
    # json.dump(encryption, open("CTF-Uppgift/db.json", "w", encoding='UTF-8'))