# LOGGING

import logging

# INFO      = 10
# DEBUG     = 20
# WARNING   = 30
# ERROR     = 40
# CRITICAL  = 50

logging.basicConfig(level=logging.INFO)

logging.info('Mensaje Informativo')
logging.debug('Mensaje de Debug')
logging.warning('Mensaje de Advertencia')
logging.error('Mensaje de Error')
logging.critical('Mensaje CRITICO!!')
