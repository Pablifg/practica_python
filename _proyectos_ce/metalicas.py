# class Cargas:
#     def __init__(self, cm, cv):
#         self.cm = cm
#         self.cv = cv
#         # Cu = self.cm * 1.2 + 1.6 * self.cv
#         # return Cu
#         qu = Cu * s
#         pass
#     pass


class Columna:
    pass


class Viga:
    pass


def cargas(cm, cv, s):
    """
    Calcula carga tributaria de frames superiores
    Cu es carga última
    s es separación entre pórticos
    cm es carga muerta
    cv es carga viva
    qu es carga distribuida

    return qu, Cu 

    """
    
    Cu = 1.2 * cm + 1.6 * cv
    qu = Cu * s
    return qu

def run():
    cm = float(input('Ingrese el valor de carga muerta: '))
    cv = float(input('Ingrese el valor de carga viva: '))
    s= float(input('Ingrese la separación entre pórticos: '))

    forces = cargas(cm, cv, s)
    print(forces)
    pass


if __name__ == '__main__':
    run()