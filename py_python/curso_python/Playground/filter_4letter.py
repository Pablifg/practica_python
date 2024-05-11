'''
Retornar solo palabras de 4 letras y más
'''

def filter_by_length(words):
    return list(filter(lambda item: len(item)>=4, words))

def run():
    words = ['amor', 'python', 'sol', 'mar', 'piedra', 'día']
    response = filter_by_length(words)
    print(response)

if __name__ == '__main__':
    run()