# -*- coding: utf-16 -*-
import random

IMAGES = ['''

        +---+
        |   |
            |
            |
            |
            |
            |
            |
            =======''', '''
        +---+
        |   |
        0   |
            |
            |
            |
            |
            |
            =======''', '''
        +---+
        |   |
        0   |
        |   |
            |
            |
            |
            |
            =======''', '''
        +---+
        |   |
        0   |
        |   |
       /    |
            |
            |
            |
            =======''', '''
        +---+
        |   |
        0   |
        |   |
       / \  |
            |
            |
            |
            =======''', '''
        +---+
        |   |
        0   |
        |   |
       /|\  |
            |
            |
            |
            =======''', '''
        +---+
        |   |
        0   |
        |   |
       /|\  |
        |   |
            |
            |
            =======''', '''
        +---+
        |   |
        0   |
        |   |
       /|\  |
        |   |
       /    |
            |
            =======''', '''
        +---+
        |   |
        0   |
        |   |
       /|\  |
        |   |
       / \  |
            |
            =======''', '''
        ''',
        ]

WORDS = [
        'guitarra',
        'piano',
        'bateria',
        'democracia',
        'teclado',
        'celular',
        'cocina',
        'machine',
        'laptop',
        'computador'
        ]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word);
    print('--- * ' * 5)


def run():
    word = random.choice(WORDS)
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        #Show board
        display_board(hidden_word, tries)
        current_letter = str(input('Write a letter: '))
        
        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 8:
                display_board(hidden_word, tries)
                print('')
                print(f'Loser! The correct word was {word}')
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print(f'Congratulation!! You are a winner. The word is: {word}')
            break


if __name__ == '__main__':
    print('B I E N V E N I D O S  A L😎  J U E G O  D E  L O S  A H O R C A D O S')
    run()
