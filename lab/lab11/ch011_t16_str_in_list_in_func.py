from typing import List

n = ["Michael", "Lieberman"]


def join_strings(words: List[str]) -> str:
    result = ""
    for word in words:
        result += word
    return result


print(join_strings(n))
