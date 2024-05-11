numbers = [1, 2, 3, 4]
numbers_v2 = []

# SIN USAR MAP
for i in numbers:
    numbers_v2.append(i * 2)

# USANDO MAP
numbers_v3 = list(map(lambda i: i * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

# Map itera dos listas y brinda tranformación de ellas
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

# Itera ambas listas y aplica lambda function para obtener la suma entre elementos
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(f'Map toma la lista con menor cantidad de elementos: {result}')
