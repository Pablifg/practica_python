# Parámetros y funciones específicos mantenidas por el intérprete
import sys
print(sys.path) #Imprime donde se está ejecuatando el archivo

# expresiones regulares
import re 
text = "Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3"

result = re.findall('[0-9]+', text) #Encontrar todo lo que esté entre 0 y 9, +: encontrar varias coincidencias
print(result)

# Manejo de horas y fechas
import time
timestamp = time.time() # hora actual de PC
print(timestamp) # Formato unix

local = time.localtime()
result = time.asctime(local) # Formato a hora legible
print(result) #fecha es hora que corre en servidor, no fecha de la máquina.

# Manejar listas
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
# Frecuencia de números
counter = collections.Counter(numbers)
print(counter) # Dict con freq de c/numero

print("ALternativa")
response = {number: numbers.count(number) for number in numbers}
print(response)