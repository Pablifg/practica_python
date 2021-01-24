# -*- coding: utf-8 -*-

#Example
#Encontrar la primera letra que no se repita adentro de un string
"""
"abacabad" c
"abacabaabacaba" _ All characters repeat
"abcdefghijklmnopqrstuvwxyznslkjfabe" d
"bcccccccccccccyb" y
"""


def first_not_repeating_char(char_sequence):
    seen_letters = {}
    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            #Uso tupla porque es estrucutra de datos ligera
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append((key, value[0]))
    
    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'


if __name__ == '__main__':
    char_sequence = str(input('Write a character secuence: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':

        print('All characters repeat')
    else:
        print(f'The first character no  repeated is: {result}')
