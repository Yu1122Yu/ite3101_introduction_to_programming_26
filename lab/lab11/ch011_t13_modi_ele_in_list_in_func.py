from typing import List

n = [3, 5, 7]

# Don't forget to return your new list!
def double_list(x: List[int]) -> List[int]:
    result = []
    for num in x:
        result.append(num * 2)
    return result
