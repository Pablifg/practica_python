# Any & Optional
## Usar cuando no conoce que tipo de dato almacenar o cuando no desea indicar un tipo -> usar Any
### No se recomienda usar Any porque permite mucha ambigüedad
### Siempre que sepas el tipo de dato, define y no uses Any
from typing import Any, Optional

x: Any
y: Any

def foo(param: Any) -> Any:
    pass

# OPTIONAL
# Definir tipos opcionales. Funciona excelente en funciones
# Es opcional porque ya tiene un valor por defecto
def foo(param: Optional[int] = 10) -> Any:
    return param

print(foo(5))
