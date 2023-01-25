import random

def dice_roll(roll_numbers, dados = 2):
    result = []
    # roll_secuence = [[random.choice([1, 2, 3, 4, 5, 6]) for i in range(roll_numbers)] for j in range(dados)]

    for _ in range(roll_numbers):
        roll = 0 #Este contador se vuelve 0 en cada fila, por lo tanto, se va sumando de nuevo generando una lista . Una fila
        for j in range(dados):
            roll += random.choice([1, 2, 3, 4, 5, 6]) #Podría usar random.randint(1,7) Es hasta el 6, 7 no inclusivo. POdría ocupar xq es entero
        result.append(roll)
    #Error cometido fue el result dentro de for j y ademas roll = 0 estaba en _.
    return result


def main(roll_numbers, try_numbers):
    #Guardar todas las veces de simulación sus resultadoss
    rolls = []

    for _ in range(try_numbers): #Corra número de intentos
        roll_secuence = dice_roll(roll_numbers) #
        rolls.append(roll_secuence)

    rolls_12 = 0
    for roll in rolls:
        # PROBABILIDAD DE OBTENER UN 12
        if 12 in roll:
            rolls_12 += 1

    roll_probabilidad_12 = rolls_12 / try_numbers
    print(f'Likelihood to get at least 12 in {try_numbers} rolls = {roll_probabilidad_12}')


if __name__ == '__main__':
    roll_numbers = int(input("How many dice rolls?: "))
    try_numbers = int(input('How many simulation try?: '))

    main(roll_numbers, try_numbers)