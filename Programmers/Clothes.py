from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)
    for item in clothes:
        clothes_dict[item[1]] += 1
    result = 1
    for count in clothes_dict.values():
        result *= (count + 1)

    return result - 1