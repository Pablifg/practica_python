# CONTEXT MANAGER

import logging
import traceback
import contextlib

logging.basicConfig(
        level=logging.ERROR,
        filename='errors.log', 
        format="%(asctime)s:%(levelname)s:%(message)s"
)


@contextlib.contextmanager
def write_on_log_error(): # Reducimos linea de code al escribir en log file
    try:
        yield # intenetar realizar todo lo que se encuentre en el bloque
        # yield es un placeholder que se reemplaza con todo lo que se encuentra en el bloque
    except Exception as error:
        exception_info = {
                'message': str(error),
                'detail': traceback.format_exc()
        }

    logging.error(exception_info)

with write_on_log_error(): 
     #result = 10 / 0
     #print(result)

     #Otro ejemplo - archivo no existe
     file = open('users.txt')

# try:
#     10 / 0 

# except Exception as error:
#     write_on_log_error(error)

# Con lo implementado, no es necesario duplicar líneas try o except para cada bloque que puede o  podría generar algún tipo de error -> mediante contextlib -> manager
