# Indicar que una variable es de tipo genérico
# Especificar que una variable es desconocida o puede variar su tipo.
# Typevar: es complejo porque trabajaremos con tipos genérico (desconocemos de qué tipo son)
from typing import TypeVar, List, Tuple, Dict

#Convención aceptada
T = TypeVar('T') # tipo genérico que tiene por nombre T

def first_element(collection: List[T]) -> T | None:
    """ Retornar el primer elemento de una colección """
    if len(collection) == 0:
        return None

    return collection[0]


print(
        first_element([1, 2, 3, 4, 5])
)

# Ejemplo: definir tipo genérico más en concreto

Number = TypeVar('Number', int, float) # <nombre de tipo> = TypeVar(<nombre_tipo>, <tipos_pertencen_a_number(genérico)>)
Collection = TypeVar('Collection', List, Tuple, Dict)


def double(number: Number) -> Number:
    return number * 2


result: Number = double(10)
print(result)
