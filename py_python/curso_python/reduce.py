import functools # Contiene a reduce

numbers = [1, 2, 3, 4]

def acumm(counter, item):
    print('counter => ', counter)
    print('item => ', item)
    return counter + item

#result = functools.reduce(lambda counter, item: counter + item, numbers)
result = functools.reduce(acumm, numbers) #Entender que hace

print(result)