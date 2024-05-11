def multiply_numbers(numbers):
    '''
    Función para multiplicar números de la lista por dos

    args:
    numbers -- lista de números

    return:
    lista de elementos multiplicados por 2
    '''
    return list(map(lambda number: number * 2, numbers))

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(numbers)
print(response)