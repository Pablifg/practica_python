# División sobre 0
# try - except
## Recomendación: Siempre indicar con qué tipo de error trabajará
## Siempre que sepa que un fragmento de código puede generar un tipo de error, coloque el fragmento de código en try, con su respectivo except.
### Ejemplo: Consumir API, conectarse a base de datos, leer archivo, enviar notificación

try:
    number_1 = 10
    number_2 = 0

    result = number_1 / number_2

    print('El resultado de la operación es: ', result)

    print('El programa ha finalizado')

except ZeroDivisionError as error:
    print('No fue posible completar la información')
    print('Tuvo un error de tipo: ', error)
