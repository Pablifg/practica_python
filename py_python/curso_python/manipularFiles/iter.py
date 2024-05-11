for i in range(1, 11):
    print(i)

# Manejar manualmente iteración
my_iter = iter(range(1,11))
## En este formato my_iter podemos controlar la manera en que se ejecuta, de forma manual.
## Iteración manual lo generamos mediante next(-)
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
'''
En rendimiento es útil porque significa que no genera rango directamente.
Lo está generando progresivamente, esto hace que los recursos en memoria no sean tan altos.

Genera a medida que ingresa al iterador mediante next()
Cuando se consumen todos los iterados y se va más allá de ese rango, genera un error de StopIteration.

Útil: en archivos los lee de esta manera.
'''
