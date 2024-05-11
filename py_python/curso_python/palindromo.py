# -*- coding: utf-8 -*-

def palindrome(word):
    word = word.replace(' ','').lower()
    reverse_word = word[::-1]
    
    if word == reverse_word:
        return True

    return False


def run(word):
    result = palindrome(word);

    if result is True:
        print(f'The word \'{word}\' > is a palindrome');
    else:
        print(f'The word \'{word}\' > isn\'t a palindrome');


if __name__ == '__main__':
    word = input('Write the word or phrase: \n');
    run(word);
