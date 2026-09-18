def solution(citations):
    answer = 0
    n = len(citations)

    for i in range(n):
        for j in range(n-i-1):
            if citations[j] > citations[j+1]:
                citations[j], citations[j+1] = citations[j+1], citations[j]

    for k in range(n):
        if citations[k] >= n-k:
            answer = n-k
            break

    return answer