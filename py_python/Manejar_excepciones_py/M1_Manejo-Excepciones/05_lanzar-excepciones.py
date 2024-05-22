# LANZAR EXCEPCIONES - raise
## Validar usuario
## Cuando se alcanza excepción, el programa termina de manera abrupta
### Para evitar-> usar try-except

def validate_username(username):

    if username == 'cody':
        raise Exception('El username no puede ser Cody.')

    if len(username) < 6:
        raise Exception('El username debe poseer una longitud mayor a 6 caracteres') # dar más contexto de xq lanzó excepción

    return True


# Validar excepción
try:
    result = validate_username('cody')
    print(result)

except Exception as error:
    print(error)
