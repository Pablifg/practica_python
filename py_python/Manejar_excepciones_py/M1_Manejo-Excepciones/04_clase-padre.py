# CLASE PADRE
## Ejecutar algo general indiferenmente del tipo de error. Realizar una sola acción por cualquier error generado. 
# Usar POO -> Herencia -> Exception -> BaseException (Clase padre)
## Lo ideal es trabajar con la clase Exception

try:
    numbers = [0, 1, 2, 3, 4, 5]

    number_1 = numbers[3]
    number_2 = numbers[0]

    result = number_1 / number_2

except Exception as error:
    print('No fue posible completar la operación.')
    print(error)

else:
    print('El resultado de la operación es: ', result)

finally:
    print('El programa ha finalizado')
