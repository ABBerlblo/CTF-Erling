import json, base64
from cryptography.fernet import Fernet

key = b'jZI7oc1mk4KXY1SA_Abg2kiLZey39jd8oATdw_CU_tE='
cipher = Fernet(key)

def decrypt(encrypted_message, salt):
    # Decode the base64-encoded message back to bytes
    encrypted_bytes = base64.urlsafe_b64decode(encrypted_message)
    # Decrypt the encrypted message using Fernet
    decrypted_message = cipher.decrypt(encrypted_bytes).decode()
    # Remove the salt to retrieve the original message
    original_message = decrypted_message[len(salt):]
    return original_message


# Decrypt info
with open("CTF-Uppgift/db.json", "r", encoding='UTF-8') as file:
    encryption_data = json.load(file)
    for user, data_list in encryption_data.items():
        for data in data_list:
            encrypted_message = data["info"]
            salt = data["salt"]

            decrypted = decrypt(encrypted_message, salt)

            # print("Encrypted Message:", encrypted_message)
            print("Decrypted Message:", decrypted)