# print(0 / 0) # -> ZeroDivisionError: division by zero
#print(result) # -> NameError
print('Hola')

suma = lambda x, y: x + y
assert suma(2,2) == 4 #se suele usar para verificar
#assert suma(2,1) == 4 #AssertionError, la función no funciona como debería

# LANZAR PROPIAS EXCEPTIONS
age = 10
if age < 18:
    raise  Exception('No se permiten menores de edad')

