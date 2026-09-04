result=[]
def solution(n, start=1, via=2, to=3):
    if n == 1:
        result.append([start, to])
        return
    
    solution(n-1, start, to, via)
    result.append([start, to])

    solution(n-1, via, start, to)
    
    return result
    

