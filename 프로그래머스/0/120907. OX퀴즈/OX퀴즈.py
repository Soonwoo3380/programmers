def solution(quiz):
    
    answer = []
    
    for item in quiz:
        left, right = item.split('=')
        if eval(left) == eval(right):
            answer.append('O')
        else:
            answer.append('X')
    
    return answer