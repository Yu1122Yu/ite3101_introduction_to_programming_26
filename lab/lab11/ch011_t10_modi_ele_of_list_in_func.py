from typing import List


def list_function(x: List[int]) -> List[int]:
    x[1] += 3
r eturn x[1]

n = [3, 5, 7]
print(list_function(n))
