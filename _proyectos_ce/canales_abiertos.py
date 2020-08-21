
class canales_abiertos:
    
    def __init__(self, y):
        self.y = y


class Rectangular(canales_abiertos):
    
    def __init__(self, y, b):
        super().__init__(y)
        # self.b = b


class Trapezoidall(canales_abiertos):
    
    def __init__(self, y):
        super().__init__(y)


class Triangular(canales_abiertos):
    
    def __init__(self, y):
        super().__init__(y)


class Circular(canales_abiertos):
    
    def __init__(self, y):
        super().__init__(y)


class Parabolica(canales_abiertos):
    
    def __init__(self, y):
        super().__init__(y)


class Rectesquina(canales_abiertos):
    
    def __init__(self, y):
        super().__init__(y)


class Trianesquina(canales_abiertos):
    
    def __init__(self, y):
        super().__init__(y)



def run():
    pass


if __name__ == '__main__':
    run()
