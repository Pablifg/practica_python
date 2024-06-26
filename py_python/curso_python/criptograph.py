# -*- coding: utf-8 -*-
import sys

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def cypher(message):
    #Generate a list whithout blank spaces
    words = message.split(' ')
    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)

    #Join cypher_message for each blank space
    return ' '.join(cypher_message)


def decypher(message):
    #Generate a list whithout blank spaces
    words = message.split(' ')
    decypher_message = []

    for word in words:
        decypher_word = ''

        for letter in word:

            for key, value in KEYS.items():
                if value == letter:
                    decypher_word += key

        decypher_message.append(decypher_word)

    #Join cypher_message for each blank space
    return ' '.join(decypher_message)


def run():

    while True:

        command = input('''--- * --- * --- * --- * --- * --- * --- * ---

        Welcome to CRYPTOGRAPHY. What do you want to do?

        [c]ipher a message
        [d]ecipher a message
        [s]alir / exit
        ''')

        if command == 'c':
            message = input('Write your message: ')
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = input('Write your message descypher: ')
            decypher_message = decypher(message)
            print(decypher_message)
        elif command == 's':
            print('Exit')
            sys.exit()
        else:
            print('Command no found!')
            

if __name__ == '__main__':
    print('C Y P H E R  M E S S A G E S')
    run()
