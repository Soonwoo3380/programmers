def solution(num, total):
    answer = [i for i in range(num)]
    
    while sum(answer) != total:
        if sum(answer) > total:
            answer = [item - 1 for item in answer]
        else:
            answer = [item + 1 for item in answer]
    
    return answer