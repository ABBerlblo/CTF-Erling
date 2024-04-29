uniqueChars = 76

def Alphabet(letter : str):
    number = 0
    if letter == 'A':
        number = 1
    elif letter == 'a':
        number = 2
    elif letter == 'B':
        number = 3
    elif letter == 'b':
        number = 4
    elif letter == 'C':
        number = 5
    elif letter == 'c':
        number = 6
    elif letter == 'D':
        number = 7
    elif letter == 'd':
        number = 8
    elif letter == 'E':
        number = 9
    elif letter == 'e':
        number = 10
    elif letter == 'F':
        number = 11
    elif letter == 'f':
        number = 12
    elif letter == 'G':
        number = 13
    elif letter == 'g':
        number = 14
    elif letter == 'H':
        number = 15
    elif letter == 'h':
        number = 16
    elif letter == 'I':
        number = 17
    elif letter == 'i':
        number = 18
    elif letter == 'J':
        number = 19
    elif letter == 'j':
        number = 20
    elif letter == 'K':
        number = 21
    elif letter == 'k':
        number = 22
    elif letter == 'L':
        number = 23
    elif letter == 'l':
        number = 24
    elif letter == 'M':
        number = 25
    elif letter == 'm':
        number = 26
    elif letter == 'N':
        number = 27
    elif letter == 'n':
        number = 28
    elif letter == 'O':
        number = 29
    elif letter == 'o':
        number = 30
    elif letter == 'P':
        number = 31
    elif letter == 'p':
        number = 32
    elif letter == 'Q':
        number = 33
    elif letter == 'q':
        number = 34
    elif letter == 'R':
        number = 35
    elif letter == 'r':
        number = 36
    elif letter == 'S':
        number = 37
    elif letter == 's':
        number = 38
    elif letter == 'T':
        number = 39
    elif letter == 't':
        number = 40
    elif letter == 'U':
        number = 41
    elif letter == 'u':
        number = 42
    elif letter == 'V':
        number = 43
    elif letter == 'v':
        number = 44
    elif letter == 'W':
        number = 45
    elif letter == 'w':
        number = 46
    elif letter == 'X':
        number = 47
    elif letter == 'x':
        number = 48
    elif letter == 'Y':
        number = 49
    elif letter == 'y':
        number = 50
    elif letter == 'Z':
        number = 51
    elif letter == 'z':
        number = 52
    elif letter == 'Å':
        number = 53
    elif letter == 'å':
        number = 54
    elif letter == 'Ä':
        number = 55
    elif letter == 'ä':
        number = 56
    elif letter == 'Ö':
        number = 57
    elif letter == 'ö':
        number = 58
    elif letter == '0':
        number = 59
    elif letter == '1':
        number = 60
    elif letter == '2':
        number = 61
    elif letter == '3':
        number = 62
    elif letter == '4':
        number = 63
    elif letter == '5':
        number = 64
    elif letter == '6':
        number = 65
    elif letter == '7':
        number = 66
    elif letter == '8':
        number = 67
    elif letter == '9':
        number = 68
    elif letter == ' ':
        number = 69
    elif letter == '.':
        number = 70
    elif letter == ':':
        number = 71
    elif letter == ',':
        number = 72
    elif letter == ';':
        number = 73
    elif letter == '!':
        number = 74
    elif letter == '?':
        number = 75
    
    return number

def InverseAlphabet(number : int):
    letter = ''
    if number == 1:
        letter = 'A'
    elif number == 2:
        letter = 'a'
    elif number == 3:
        letter = 'B'
    elif number == 4:
        letter = 'b'
    elif number == 5:
        letter = 'C'
    elif number == 6:
        letter = 'c'
    elif number == 7:
        letter = 'D'
    elif number == 8:
        letter = 'd'
    elif number == 9:
        letter = 'E'
    elif number == 10:
        letter = 'e'
    elif number == 11:
        letter = 'F'
    elif number == 12:
        letter = 'f'
    elif number == 13:
        letter = 'G'
    elif number == 14:
        letter = 'g'
    elif number == 15:
        letter = 'H'
    elif number == 16:
        letter = 'h'
    elif number == 17:
        letter = 'I'
    elif number == 18:
        letter = 'i'
    elif number == 19:
        letter = 'J'
    elif number == 20:
        letter = 'j'
    elif number == 21:
        letter = 'K'
    elif number == 22:
        letter = 'k'
    elif number == 23:
        letter = 'L'
    elif number == 24:
        letter = 'l'
    elif number == 25:
        letter = 'M'
    elif number == 26:
        letter = 'm'
    elif number == 27:
        letter = 'N'
    elif number == 28:
        letter = 'n'
    elif number == 29:
        letter = 'O'
    elif number == 30:
        letter = 'o'
    elif number == 31:
        letter = 'P'
    elif number == 32:
        letter = 'p'
    elif number == 33:
        letter = 'Q'
    elif number == 34:
        letter = 'q'
    elif number == 35:
        letter = 'R'
    elif number == 36:
        letter = 'r'
    elif number == 37:
        letter = 'S'
    elif number == 38:
        letter = 's'
    elif number == 39:
        letter = 'T'
    elif number == 40:
        letter = 't'
    elif number == 41:
        letter = 'U'
    elif number == 42:
        letter = 'u'
    elif number == 43:
        letter = 'V'
    elif number == 44:
        letter = 'v'
    elif number == 45:
        letter = 'W'
    elif number == 46:
        letter = 'w'
    elif number == 47:
        letter = 'X'
    elif number == 48:
        letter = 'x'
    elif number == 49:
        letter = 'Y'
    elif number == 50:
        letter = 'y'
    elif number == 51:
        letter = 'Z'
    elif number == 52:
        letter = 'z'
    elif number == 53:
        letter = 'Å'
    elif number == 54:
        letter = 'å'
    elif number == 55:
        letter = 'Ä'
    elif number == 56:
        letter = 'ä'
    elif number == 57:
        letter = 'Ö'
    elif number == 58:
        letter = 'ö'
    elif number == 58:
        letter = 'ö'
    elif number == 59:
        letter = '0'
    elif number == 60:
        letter = '1'
    elif number == 61:
        letter = '2'
    elif number == 62:
        letter = '3'
    elif number == 63:
        letter = '4'
    elif number == 64:
        letter = '5'
    elif number == 65:
        letter = '6'
    elif number == 66:
        letter = '7'
    elif number == 67:
        letter = '8'
    elif number == 68:
        letter = '9'
    elif number == 69:
        letter = ' '
    elif number == 70:
        letter = '.'
    elif number == 71:
        letter = ':'
    elif number == 72:
        letter = ','
    elif number == 73:
        letter = ';'
    elif number == 74:
        letter = '!'
    elif number == 75:
        letter = '?'
    
    return letter