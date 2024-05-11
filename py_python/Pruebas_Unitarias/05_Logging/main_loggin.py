import logging # por default solo imprime msg en consola > 30. 

# 5 TIPOS DE MENSAJES
## DEBUG = 10
## INFO = 20
## WARNING  = 30
## ERROR = 40
## CRITICAL = 50

# Se encuentran ordenados de acuerdo a nivel de prioridad
# Por lo tanto, Debug menos importante y Critical más importante

#logging.basicConfig(level=20) # Modificar el comportamiento default de logging para indicar desde q nivel queremos visualizar msg
## Cambiando el formato
logging.basicConfig(level=logging.INFO,
        format="%(threadName)s - %(levelname)s - %(asctime)s - Message:%(message)s", #process, processName, thread, threadName
                    datefmt="%Y/%m/%d",#formato fechas
                    # Almacenar loggings - No se imprimen en consola pero se almacenan líneas al .log
                    filename="register.log",
                    filemode="a" # añadirse todos los log al final del archivo
                )

def suma (numero1: int, numero2:int) -> int:
    """Permite sumar 2 números enteros.

    Args:
        numero1 (int):
        numero2 (int):

    Returns:
        : int
    """

    logging.debug('Entramos aquí!!!')
    
    resultado = numero1 + numero2

    logging.debug('Nos encontramos en esta línea.')

    return resultado


if __name__ == '__main__':
    logging.debug('Antes del llamado de la función.')

    resultado = suma(15, 20)
    logging.info(resultado)
    # Out: INFO:<quien_imprimio(user)>:resultado | formato se puede modificar

