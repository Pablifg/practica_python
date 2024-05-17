# ALIAS
# Reducir líneas de código mediante alias, logrando que código sea más legible
# Alias = <combinación_tipos>

from typing import Tuple

UserIdi = int
Book = Tuple[str, str, int]
UserIdorNone = int | None


def database_connection(
        connection: Tuple[str, str,int]
        ) -> Tuple[str, str, int] | None:

    if connection[0] != 'root':
        return None

    return connection

connection: Tuple[str, str, int] = ('root', 'codigofacilito', 3306)

print(database_connection(connection))

# Cuando definamos tipos complejos, definir ALIAS
ConnectionType = Tuple[str, str, int]

def database_connection(connection: ConnectionType) -> ConnectionType | None:

    if connection[0] != 'root':
        return None

    return connection

connection: ConnectionType = ('camavinga', 'plaza', 3306)
print(database_connection(connection))
