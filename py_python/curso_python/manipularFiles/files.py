file = open('./text.txt')
'''
#print(file.read()) # Leer archivo completo. Bueno para archivos con poca info. Caso contrario, ocupa memoria
print(file.readline()) # Leer línea por línea. Funciona como el iterador. Va lína por línea hasta temrinar
print(file.readline()) # Es ligero en cuanto a consumo de memoria
print(file.readline())
print(file.readline()) # Similiar a iteradores

# Para leer todo el archivo y que no sea muy pesado para evitar bloqueo en memoria
'''
for line in file:
    print(line)


# Cuado deja de trabajar con el archivo, SIEMPRE deberá cerrar
file.close() # Libera espacio de memoria en Python para no mantener el archivo abierto.

# SINTÁXIS PARA QUE PYTHON AUTOMÁTICAMENTE ABRA Y CIERRE EL ARCHIVO -- Forma más común que se usa en python
with open('./text.txt') as file:
    for line in file:
        print(line)
