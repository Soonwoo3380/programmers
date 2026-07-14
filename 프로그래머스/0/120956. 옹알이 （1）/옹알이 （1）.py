def solution(babbling):  
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    
    for item in babbling:
        for word in words:
            item = item.replace(word, " ")
            
        if item.strip() == "":
            answer += 1
        
    return answer