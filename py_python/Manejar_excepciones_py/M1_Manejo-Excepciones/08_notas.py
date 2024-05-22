# AÑADIR NOTAS A EXCEPCIONES QUE LANCEMOS
## Esto da más contexto a desarrolladores de la razón por la cuál fue lanzada la excepción
# +3.11 python

class UsernameException(Exception):

    def __init__(self):
        super().__init__('El username no es válido.')

    def is_valid_to_raise(self):
        return len(self.__notes__) > 0

    def show_notes(self):
        for note in self.__notes__:
            print('>>> ', note)


# Definir fucnión que permita validar el username
def username_validation(username):
    
    username_error = UsernameException()

    if len(username) <= 5:
        username_error.add_note('La longitud debe ser mayor a 5.')

    if username.lower() == 'cody':
        username_error.add_note('El usernanme no puede ser Cody')

    if '@' in username:
        username_error.add_note('El signo @ no puede encontrarse en el username.')

    # Conocer si una exception contiene notas
    if username_error.is_valid_to_raise(): #__notes__: # Los atributos que sean __<some>__ NO USAR FUERA DE LA CLASE. Preferible crear método en clase para usarlo
        raise username_error

    return True


#Usando bloque TRY-EXCEPTION para manejar el error
try:
    username = 'Cody'
    username_validation(username)

except UsernameException as error:
    print(error)
    error.show_notes()
