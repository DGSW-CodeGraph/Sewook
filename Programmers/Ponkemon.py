def solution(nums):
    answer = 0
    pks = len(nums) // 2
    temp = []
    for i in nums:
        if i not in temp and len(temp) < pks:
                temp.append(i)
        if len(temp) >= answer:
            answer = len(temp)
    return answer