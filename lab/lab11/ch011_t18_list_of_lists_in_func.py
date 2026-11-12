from typing import List


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]


def flatten(lists: List[List[int]]) -> List[int]:
    result = []
    for inner_list in lists:
        for item in inner_list:
            result.append(item)
    return result


print(flatten(n))
