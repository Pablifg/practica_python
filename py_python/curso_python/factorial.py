# -*- coding: utf-8 -*-
def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)



def run(number):
    result = factorial(number)
    print(f'The factorial of {number} is {result}')


if __name__ == '__main__':
    number = int(input('Write a number: '))
    run(number)
