# -*- coding: UTF-8 -*-

def prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            print("Hi")
            print(i)
            if number % i == 0:
                return False

    return True


def main():
    number = int(input('Write a numbe: '))
    result = prime(number)

    if result is False:
        print(f'Your number {number} is\'nt prime')
    elif result is True:
        print(f'Your number {number} is prime')


if __name__ == '__main__':
    main()
