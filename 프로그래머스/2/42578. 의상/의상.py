def solution(clothes):
    clothes_dict = {}
    
    for key, value in clothes:
        if value in clothes_dict:
            clothes_dict[value] += 1
        else:
            clothes_dict[value] = 1
            
    answer = 1
    
    for count in clothes_dict.values():
        answer *= count + 1
        
    return answer - 1
    