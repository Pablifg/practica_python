# GRUPO DE EXCEPCIONES - Múltiples excepciones al mismo tiempo
# +3.11 python

from exceptions import CustomError1, CustomError2, CustomError3


try: # manejar grupo de excepciones
# Lanzar grupo de excepciones
    raise ExceptionGroup(
         'Un grupo de errores propios', #str donde describe el grupo
         [CustomError1(), CustomError2(), CustomError3()] #listado de excepciones a lanzar en conjunto
    )
#except ExceptionGroup as group:
#    print(group)

# También los puede trabajar de manera individual el error que está en el grupo de errores
## Desempaquetar usando *
except *CustomError1 as error:
    print('Error de tipo 1')

except *CustomError2 as error:
    print('Error de tipo 2')

except *CustomError3 as error:
    print('Error de tipo 3')
    print(error)

# Ejemplos: conectarse a bd puede lanzar grupo de excepciones de manera individual, generar tickets, etc
