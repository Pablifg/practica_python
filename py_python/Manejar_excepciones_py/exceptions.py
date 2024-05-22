class UsernameCodyException(Exception): # Sufijo excepctione s opcionla, pero lo recomienda usar
    
    def __init__(self):
        self.message = 'El username no puede ser Cody'
        super().__init__(self.message)


class UsernameLenException(Exception):
    
    def __init__(self, username):
        self.message = f'El username {username} debe poseer una longitud mayor igual a 6.'
        super().__init__(self.message)



class CustomError1(Exception):

    def __init__(self):
        super().__init__('Error número 1')


class CustomError2(Exception):

    def __init__(self):
        super().__init__('Error número 2')
class CustomError3(Exception):

    def __init__(self):
        super().__init__('Error número 3')
