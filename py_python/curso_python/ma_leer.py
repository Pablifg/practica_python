#Manipular texto de aleph.txt
#Contar cuantas veces dentro de texto se utiliza la palabra Beatriz


def run():
    #Abrir texto
    counter = 0;
    with open('./aleph.txt') as f:
        for line in f:
            counter += line.count('Beatriz')

    print(f'Beatriz se encuentra {counter} veces en el texto')


if __name__ == '__main__':
    run()
