# Crear clases inmutables. No se modificarán en tiempo de ejecución
# -Esta es una feature que lanzará error de Atributo en caso de intentar modificar atributos de la clase inmutable
# Clases heredarán de NamedTuple -> una vez creados, no podrán ser modificados

from typing import NamedTuple, Literal

class DataBaseSetting(NamedTuple):
    username: str
    password: str | None
    port: Literal[3306, 5000, 8000, 3000]
    database: str


# Instanciar n cantidad de objetos que desee
database_config_1 = DataBaseSetting(
        'root',
        'password123',
        3306,
        'own_dataset'
        )

# Podemos consultar cada uno de los atributos
print(database_config_1.username)
print(database_config_1.password)
print(database_config_1.port)
print(database_config_1.database)

# Ejemplo donde lanzará error
database_config_1.username = 'newbee'
