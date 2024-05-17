# Estructura <variable>: <tipo_estructura> = ...  --> Ojo, es : seguidos en la variable

numbers: list = [1, 2, 3] # Lista
names: tuple = ('user1', 'user2') # Tupla
scores: dict = {'cody': 100, 'faisy': 70} # Diccionario

print(numbers)
print(names)
print(scores)

# Otra manera de definir que una lista o tupla contendrá SOLO datos del mismo tipo
from typing import List, Tuple, Dict # Importando clases - Sirvern para indicar que tipo de dato almacenará la estructura

numbers: List[int] = [1, 2, 3]
names: Tuple[str, str] = ('user1', 'user2')
scores: Dict[str, int] = {'user1': 100, 'user2': 70} # [llave, valores] -> por llabe string y por valores enteros

print('*'*10 + 'Typing' + '*'*10)
print(numbers)
print(names)
print(scores)

# RECUERDA: esto no afecta al intérprete, solo es informativo para el usuario
