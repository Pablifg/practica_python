# EVITAR USAR (AUNQUE PUEDEN EXISTIR CASOS PUNTUALES).

try:
    raise Exception('No es posible continuar.')

except Exception as error:
    pass # Dejar vacío para que no se notifique que existió error.

finally:
    print('Finalizamos el bloque')


print('Finalizamos el programa')

# OTRA MANERA - AUNQUE SE RECOMIENDA USAR LA ANTERIOR
from contextlib import suppress

with suppress(Exception): # se coloca la clase entre (), Ex: (ZeroDivision)
    result = 10 / 0
    print(result)


print('Finalizamos el programa de forma correcta')
