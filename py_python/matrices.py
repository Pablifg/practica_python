#It's a text line for fix-typo. No fix. just practice.

#Print matrix
def show_matrix(matriz):
    for fila in matriz:
        print(fila)

#Dada la matriz
matriz = [
    [13, 15, 23, 87, 11],
    [81, 14, 16, 33, 44],
    [51, 10, 17, 19, 25],
    [31, 36, 41, 88, 99],
]

#Show original matrix
show_matrix(matriz)
print('---' * 20)

rows = len(matriz)
cols = len(matriz[0])
print(f'Matrix is {rows} x {cols}')
print('---' * 20)

#save in a new list
sum_row = []
for i in range(rows):
    suma = sum(matriz[i]) #suma elementos de matriz fila
    sum_row.append(suma) #Create a new element in matrix

print(f'Sum is the next list: {sum_row}')
print('---' * 20)

#Save rows sum in end matrix
for i in range(rows):
    suma = sum(matriz[i]) #suma elementos de matriz fila
    matriz[i].append(suma) #Create a new element in matrix

#Show modified matrix
show_matrix(matriz)
print('---' * 20)

#Save in a new list (colums sum)
sum_cols = []
for j in range(cols):
    suma = sum([fila[j] for fila in matriz])
    sum_cols.append(suma)

print(f'Sum is the next list: {sum_cols}')
print('---' * 20)

#Save sum list end
sum_cols.append(sum(sum_cols))
print(f'Sum is the next list: {sum_cols}')
print('---' * 20)
