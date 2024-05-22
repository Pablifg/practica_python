# GENERAR ARCHIVOS LOGS A PARTIR DE EXCEPCIONES OCURRIDAS EN TIEMPO DE EJECUCIÓN

import logging

# Almacenar en archivo de sistema
logging.basicConfig(
        level=logging.ERROR,
        filename='errors.log', #None-> se imprime en consola | si asigna nombre, se guarda en archivo. El archivo es "a", se añade al final y no se sobreescribe los logs de error.
)
# Fin configuración de almacen en sistema

try:
    10 / 0 

except Exception as error:
    logging.error('No es posible completar la operación')
    print(error)

