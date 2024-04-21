# CTF-Erling

My flag will be hidden by a salt encryption algorithm written in Python.

## CTF Folder
- `Encoder.py`: Encrypts user input and writes the encrypted message to a file.
- `Decoder.py`: Reads the encrypted message from the file and decrypts it.
- `Cypher.py`: Contains the custom cipher algorithm used for encryption.
- `Decypher.py`: Contains the decryption algorithm.
- `SaltGenerator.py`: Generates a random salt used in encryption.
- `Alphabet.py`: Contains functions to map characters to numbers and vice versa.

How It Works:

1. The `Encoder.py` script takes user input, generates a random salt using `SaltGenerator.py`, encrypts the input message using the custom cipher algorithm from `Cypher.py`, and writes the encrypted message to a file named `Output.txt`.
2. The `Decoder.py` script reads the encrypted message from `Output.txt`, extracts the salt and the encrypted message, and decrypts the message using the decryption algorithm from `Decypher.py`.
3. The cipher algorithm in `Cypher.py` shifts each character in the input message by an amount determined by the salt, while the decryption algorithm in `Decypher.py` reverses this shift to obtain the original message.

## CTF-Uppgift Folder

When I am done writing and testing the encryption, it will be implemented as a CTF task in this folder.
