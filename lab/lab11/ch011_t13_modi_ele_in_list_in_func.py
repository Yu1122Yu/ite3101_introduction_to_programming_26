from typing import List

n = [3, 5, 7]

# Don't forget to return your new list!
def double_list(x: List[int]) -> List[int]:
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print(double_list(n))

print(double_list(n))
