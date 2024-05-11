# -*- coding: UTF-8 -*-
def foreign_exchange_calculador(ammount):
    dol_to_col = 3428.8

    return dol_to_col * ammount



def main():
    print('C A L C U L A D O R A   D E   D I V I S A S ')
    print('Mexican peso to Colombian peso')
    print('')

    ammount = float(input('Ingresa cantidad de dólares que desea convertir: '))

    result = foreign_exchange_calculador(ammount)
    print(f'${ammount} dólares son ${result} pesos colombianos')
    print('')


if __name__ == '__main__':
    main()
    print('Final')
