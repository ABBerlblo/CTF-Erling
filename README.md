# CTF-Erling

## Overview

This project focuses on creating a Capture The Flag (CTF) challenge centered around a salt encryption algorithm written in Python. The first challenge involves finding and decrypting a link to the flag from a database by reverse-engineering the encryption algorithm consisting of a Fernet cipher and salt. The second challenge involves finding a new, added flag in the same database when it has been hashed instead of encrypted with a Fernet cipher.

### Files

- `information.txt`: Contains a list of strings, both decoy information and the hidden link.
- `information2.txt`: Contains a list identical to `information.txt`, but the second flag has been added.
- `solution.txt`: A link to the website with the first flag and second challenge.
- `Plannering.docx`: My initial project plan.

## public Folder

A website hosted on Firebase that contains the flag for the first challenge and a option to download the second version.

### Files

- `index.html`: The website with the flag.
- `CTF-Uppgift2.zip`: The second version.

## CTF

### Acceleration Folder

Various attempts to speed up the process of finding hashed matches, all ultimately unused.

### Files

- `Solver2GPU.py`: Attempt at using CUDA cores.
- `Solver2Torch.py`: Same as `Solver2GPU.py` but with a different approach using the Torch module.
- `test.cpp`: Attempt at rewriting solver 2 in C++.

### Test Folder

Exploration of possible salt generation methods, leading to the decision to use another method (see `salty.py`).

### Files

- `Encoder.py`: Encrypts user input and writes the encrypted message to `Output.txt`.
- `Decoder.py`: Reads the encrypted message from `Output.txt` and prints the decryption.
- `Cypher.py`: Contains a custom cipher algorithm used for encryption.
- `Decypher.py`: Contains a decryption algorithm.
- `SaltGenerator.py`: Generates a random salt used in encryption.
- `Alphabet.py`: Contains functions to map characters to numbers and vice versa.
- `Output.txt`: File containing the encrypted message.

How it works:

1. The `Encoder.py` script takes user input, generates a random salt using `SaltGenerator.py`, encrypts the input message using the custom cipher algorithm from `Cypher.py`, and writes the encrypted message to a file named `Output.txt`.
2. The `Decoder.py` script reads the encrypted message from `Output.txt`, extracts the salt and the encrypted message, and decrypts the message using the decryption algorithm from `Decypher.py`.
3. The cipher algorithm in `Cypher.py` shifts each character in the input message by an amount determined by the salt, while the decryption algorithm in `Decypher.py` reverses this shift to obtain the original message.

## CTF-Uppgift Folder

The `CTF-Uppgift` folder contains the implementation of a Capture The Flag (CTF) challenge centered around a salt encryption algorithm. The challenge involves decrypting a link to the flag. The link is hidden within a simple JSON database.

### Files

- `main.py`: The main script for the CTF challenge, responsible for encrypting information from `information1.txt`and storing it in `db.json`.
- `salty.py`: Function that generates a random salt, taking an int as an argument for the length of the salt.
- `db.json`: JSON file containing encrypted user information with corresponding salts.
- `Your_Task.md`: A story with some guidelines to solving the task.
- `salty-raining-salt.gif`: Contains a gif for `Your_Task.md`.

How it works:

- The `main.py` script reads information from `information.txt`, encrypts it using a Fernet encryption scheme with a unique salt generated from `salty.py` for each entry, and stores the encrypted data along with the salts in `db.json`.
- The `information.txt` will not be available to the challenger; hence, they must decrypt the encrypted data in `db.json` using their own decryption algorithm to reveal the flag.

## CTF-Uppgift 2 Folder

The `CTF-Uppgift 2` folder contains the second version of the challenge centered around a salted hash encryption algorithm. The challenge involves finding the matching hash for the flag and by extention the flag. The flag is added to the `information.txt` to create `information2.txt` which creates the new `db.json` after `main.py` has run.

### Files

- `main.py`: The main script for the CTF challenge, responsible for encrypting information from `information2.txt` and storing it in `db.json`.
- `salty.py`: Function that generates a random salt, taking an int as an argument for the length of the salt.
- `db.json`: JSON file containing encrypted user information with corresponding salts.
- `Your_Task.md`: Specifies the changes and the new goal.
- `salty-raining-salt.gif`: Contains a gif for `Your_Task.md`.

How it works:

- The `main.py` script reads information from `information2.txt`, concatenates the info with a unique salt generated from `salty.py` for each entry, hashes it using SHA-256, and stores the hash along with the salts in `db.json`.
- The `information2.txt` will not be available to the challenger; hence, they must decrypt the encrypted data in `db.json` using their own decryption algorithm to reveal the flag.
- By using their solution algorithm from the first challenge to get the information from `information.txt` the challenger should be able to find the odd hash containging the flag fairly easy.

## CTF-Uppgift solver Folder

This folder contains possible decryption solutions for both encryption scripts.

### Files

- `solver.py`: The decryption script for the CTF challenge, decrypts the information stored in `db.json`.
- `solver2.py`: The decryption script for the second version; decryption only applies to the hashed version of the flag.

How it works:

- The `solver.py` script reads information from `db.json`, decrypts it using the key to the Fernet encryption scheme and the unique salt generated from `salty.py` for each entry, and prints the decrypted info to the terminal.
- The `solver2.py` needs the hash, salt, and length of the "inner string" (210S{xxxxxx}, the inner string is 6 in this case) of the flag to work. The script iterates through all possible combinations of lowercase letters with the length of the "inner string" and combines these with the salt and the fingerprint for the flag, as such: salt + 210S{specific combination}. This new string is then hashed and compared to the target hash. If they match, the matching string is returned along with the time taken to find it.
