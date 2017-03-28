import string

alphabet_dictionary = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
upper_char = string.ascii_uppercase
lower_char = string.ascii_lowercase

def alphabet_position(letter):
    lc_letter = letter.lower()
    position = alphabet_dictionary[lc_letter]

    return position

def rotate_character(char, rot):
    if char.isalpha():
        char_position = alphabet_position(char) #get character position (value)

        if char in upper_char:                  #get rotated position (value)
            rot_position = (int(upper_char.find(char)) + rot) % 26
        if char in lower_char:
            rot_position = (int(lower_char.find(char)) + rot) % 26

        rot_position_char = list(alphabet_dictionary.keys())[list(alphabet_dictionary.values()).index(rot_position)] #get character (key) at that rotated position (value)

        if char in upper_char: #if the originally entered character was uppercase
            rot_position_char = rot_position_char.upper()   #convert rotated position character to uppercase

        return rot_position_char

    else:
        return char

def encrypt(text, rot):
    encrypted_string = ""
    for i in text:
        encrypt_position_char = rotate_character(i, rot)
        encrypted_string += encrypt_position_char

    return encrypted_string
