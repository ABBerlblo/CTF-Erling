# The importance of Salt

![](/CTF-Uppgift/salty-raining-salt.gif)

In the heart of a bustling city, a group of aspiring hackers gathered in a dimly lit room. They were tasked with cracking a challenging Capture The Flag challenge that had been circulating underground forums for weeks.

Eager to prove your skills in the world of cybersecurity, you eagerly accepted the challenge. The task centered around a mysterious set of scripts: main.py, salty.py, and a file named db.json. Rumor had it that the key to victory lay within the encrypted contents of db.json, which was said to contain a link leading to the coveted flag.

As you studied the scripts meticulously, you quickly recognized the encryption scheme utilized in main.py: Fernet encryption with a unique salt for each entry. Though the encrypted data in db.json seemed impenetrable at first glance, but you received word from a trusted source that someone had successfully reverse-engineered the key to the Fernet cipher. With this revelation, the pressure of time weighed heavily on your shoulders. You knew that others would soon catch wind of the breakthrough, and the race to claim the flag would only intensify. Despite the looming threat of competitors, your determination to crack the encryption only grew stronger with each passing moment.

Armed with your coding prowess and fueled by the challenge, you dove headfirst into decrypting the contents of db.json. Each encrypted entry posed a new puzzle to solve, but you were undeterred. With each success, you felt yourself inching closer to uncovering the elusive flag.
