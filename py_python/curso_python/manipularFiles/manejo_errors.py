'''
try:
    print(0 / 0)
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1, 'Uno no es igual a uno'
except AssertionError as error:
    print(error)

# Capturar exception propia
try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except Exception as error:
    print(error)
'''
# Unificando try-exception
try:
    print(0 / 0)
    assert 1 != 1, 'Uno no es igual a uno'
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print('Hola')