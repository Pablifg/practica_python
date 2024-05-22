# Puede tener N cantidad de bloques de except, según lo requiera

try:
    numbers = [0, 1, 2, 3, 4, 5]

    number_1 = numbers[0]
    number_2 = numbers[10]

    result = number_1 / number_3

except ZeroDivisionError as error:
    print('No fue posible Dividir para cero')
    print('Tuvo un error de tipo: ', error)

except NameError as error:
    print('La variable no se encuentra definida')
    print(error)

except IndexError as error:
    print('No es posible acceder al índice')
    print(error)

else:
    print('El resultado de la operación es: ', result)

finally:
    print('El programa ha finalizado')
