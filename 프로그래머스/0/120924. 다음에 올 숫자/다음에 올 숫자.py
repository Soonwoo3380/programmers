def solution(common):
    answer = 0
    sum_common = sum(common)
    if (len(common) * (common[0] + common[-1])) / 2 == sum_common:
        answer = common[-1] + (common[1] - common[0])
    else:
        answer = common[-1] * (common[1] // common[0])
    
    return answer