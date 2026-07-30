def solution(arr):

    answer = []

    for compare in arr:
        if len(answer) == 0 or answer[-1] != compare:
            answer.append(compare)

    return answer