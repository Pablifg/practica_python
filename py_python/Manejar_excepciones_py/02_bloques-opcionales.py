# Bloques opcionales: else, finally

try:
    number_1 = 10
    number_2 = 2

    result = number_1 / number_2

except ZeroDivisionError as error:
    print('No fue posible completar la información')
    print('Tuvo un error de tipo: ', error)

else:
    print('El resultado de la operación es: ', result)

finally:
    print('El programa ha finalizado')

