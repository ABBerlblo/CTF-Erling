# CTF-Erling

## Overview

This project focuses on creating a Capture The Flag (CTF) challenge centered around a salt encryption algorithm written in Python. The challenge involves finding and decrypting a flag from a database by reverse-engineering the encryption algorithm consisting of a fernet cipher and salt.

### Files

- `information.txt`: Contains a list of info with the hidden flag.
- `solution.txt`: A link to the flag.
- `Plannering.docx`: My initial project plan

## public Folder

A website that is hosted on firebase, contains the flag.

### Files

- `index.html`: The website with the flag.

## CTF Test Folder

Me playing around with possible salt generation methods. In the end I decided to use another (see `salty.py`).

### Files

- `Encoder.py`: Encrypts user input and writes the encrypted message to `Output.txt`.
- `Decoder.py`: Reads the encrypted message from `Output.txt` and prints the decryption.
- `Cypher.py`: Contains a custom cipher algorithm used for encryption.
- `Decypher.py`: Contains a decryption algorithm.
- `SaltGenerator.py`: Generates a random salt used in encryption.
- `Alphabet.py`: Contains functions to map characters to numbers and vice versa.
- `Output.txt` : File containing the encrypted message

How it works:

1. The `Encoder.py` script takes user input, generates a random salt using `SaltGenerator.py`, encrypts the input message using the custom cipher algorithm from `Cypher.py`, and writes the encrypted message to a file named `Output.txt`.
2. The `Decoder.py` script reads the encrypted message from `Output.txt`, extracts the salt and the encrypted message, and decrypts the message using the decryption algorithm from `Decypher.py`.
3. The cipher algorithm in `Cypher.py` shifts each character in the input message by an amount determined by the salt, while the decryption algorithm in `Decypher.py` reverses this shift to obtain the original message.

## CTF-Uppgift Folder

The `CTF-Uppgift` folder contains the implementation of a Capture The Flag (CTF) challenge centered around a salt encryption algorithm. The challenge involves decrypting a link to the flag. The flag is hidden within a simple json dastabase.

### Files

- `main.py`: The main script for the CTF challenge, responsible for encrypting information and storing it in `db.json`
- `salty.py`: Function that generates a random salt, takes an int as an argument for the lenght of the salt.
- `db.json`: JSON file containing encrypted user information with corresponding salts.
- `Your_Task.md`: A story with some guidelines to solving the task.
- `salty-raining-salt.gif`: Contains a gif for `Your_Task.md`.

How it works:

- The `main.py` script reads information from `information.txt`, encrypts it using a Fernet encryption scheme with a unique salt generated from `salty.py` for each entry, and stores the encrypted data along with the salts in `db.json`.
- The `information.txt` will not be available to the class, hence they must decrypt the encrypted data in `db.json` using their own decryption algorithm to reveal the flag.

## CTF-Uppgift solver Folder

The `CTF-Uppgift solver` folder contains a possible decryption script.

### Files

- `solver.py`: The main script for the CTF challenge, responsible for encrypting information and storing it in `db.json`

How it works:

- The `solver.py` script reads information from `db.json`, decrypts it using a the key to the Fernet encryption scheme and the unique salt generated from `salty.py` for each entry, and prints the decrypted info to the terminal.
