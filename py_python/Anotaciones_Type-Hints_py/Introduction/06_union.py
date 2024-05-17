# UNION para definir que una variable puede tomar diferentes tipos de datos
# usa unión cuando sepas que tendrá varios tipos de datos y no sabes cuál tendrá de los varios tipos
from typing import Union, List

username: Union[None, str]


def average(numbers: List[int]) -> Union[None, float]:

    if len(numbers) == 0:
        return None

    return sum(numbers) / len(numbers)


numbers = []
#result: Union[None, float] = average(numbers)
result: None | float = average(numbers)
print(result)

# En versiones actuales de python (+3.9), en vez de:
# Union[None, float] -> usar: None | float
