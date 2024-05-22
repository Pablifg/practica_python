# FORMATO DE LOGS - Cambiar a formato que desee

import logging
import traceback

logging.basicConfig(
        level=logging.ERROR,
        filename='errors.log', 
        format="%(asctime)s:%(levelname)s:%(message)s" # Indicar el formato que desaea usar para los mensajes
)

try:
    10 / 0 

except Exception as error:
    exception_info = { # diccionario para almacenar toda la info de la excepción lanzada
            'message': str(error),
            'detail': traceback.format_exc()
}
    # logging.error( str(error) ) # convertir error en string y sea str el que se almacene
    logging.error(exception_info)

# Captura el traceback para conocer los pasos que ocurrieron para que el error suceda. Esto nos permite replicar el error
