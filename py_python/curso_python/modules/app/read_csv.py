import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader) # columnas. La primera fila son los header en este archivo .csv
        #print(header)
        data = []
        # Leer fila a fila
        for row in reader:
            # Unir 2 arrays con ZIP
            iterable = zip(header, row) # Une en array de tuplas.
            # print(list(iterable))
            #Generar diccionario a partir de iterable
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)

            # print('***' * 5)
            # print(row)

        return data # array que con diccionarios

# RETO: TRANSFORMARLO A DICCIONARIO PARA LECTURA MÁS SENCILLA
## Su key debe ser el nombre de la columna y el value la row
## Necesita retornar lista con todos los diccionarios
## Permite hacer consulta de forma más precisa a la info :D


# Correr como script desde terminal
if __name__ == '__main__':
    data = read_csv('./data.csv')
    print(data)