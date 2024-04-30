# The Importance of Salt

![Salty Raining Salt](/CTF-Uppgift/salty-raining-salt.gif)

Congratulations on solving the first flag! I suppose it wasn't too difficult of a task; some might even call it easy. However, the security provided by the salt in the previous task was rendered ineffective when someone could easily reverse the Fernet cipher. Therefore, for this flag, the encryption method has been changed from Fernet to hashing with SHA-256.

A new flag has been added to the file `information2.txt`, which is otherwise identical to `information.txt`. As usual, you do not have access to this file. The flag has the format "210S{xxxxxx}" where 'x' is 6 different; arbitrary lowercase letter. The flag could for example be "210S{pepper}".

Good luck!
