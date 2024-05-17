from typing import List

def average(numbers: List[int]) -> float : # float es el valor a retornar
    return sum(numbers) / len(numbers)


scores: List[int] = [10, 10, 9, 8, 8, 8]
result: float = average(scores)

print(result)


def _sum(number_1: int, number_2: int) -> int:
    return number_1 + number_2


result = _sum(10, 20)
print(result)
