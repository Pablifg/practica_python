# -*- coding: UTF-8 -*-

import turtle

def main():
    windows = turtle.Screen()
    pablo = turtle.Turtle()

    make_square(pablo)

    turtle.mainloop()


def make_square(pablo):
    lenght = int(input('Tamaño de cuadrado: '))
    
    for i in range(4):
        make_line_and_turn(pablo, 100)


def make_line_and_turn(pablo, lenght):
    pablo.forward(lenght)
    pablo.left(90)



if __name__ == '__main__':
    main()

