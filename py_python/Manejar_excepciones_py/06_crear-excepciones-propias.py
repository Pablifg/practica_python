# CREAR PROPIAS EXCEPCION
# Mediante POO y lanzarlas cuando deseemos
## Usaremos clases -> Deben heredar de Exception (clase "padre")
## Consejo: tener archivo de nuestras propias exceptiones donde únicamente almacenemos nuestras clases para las excepciones

#class UsernameCodyException(Exception): # Sufijo excepctione s opcionla, pero lo recomienda usar
    
#    def __init__(self):
#        self.message = 'El username no puede ser Cody'
#        super().__init__(self.message)


#class UsernameLenException(Exception):
    
#    def __init__(self, username):
#        self.message = f'El username {username} debe poseer una longitud mayor igual a 6.'
#        super().__init__(self.message)

from exceptions import UsernameCodyException, UsernameLenException

def validate_username(username):

    if username == 'cody':
        raise UsernameCodyException()

    if len(username) < 6:
        raise UsernameLenException(username) 

    return True


# Validar excepción
try:
    result = validate_username('cody1')
    print(result)

except UsernameCodyException as error:
    #print('El username no puede ser Cody')
    print(error)

except UsernameLenException as error:
    #print('La longitud del username no es válida')
    print(error)

except Exception as error:
    print(error)
    print('>>> No fue posible completar la operación')
