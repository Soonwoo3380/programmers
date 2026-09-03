def solution(participant, completion):
    map = {}
    
    for i in participant:
        map[i] = map.get(i, 0) + 1
        
    for j in completion:
        map[j] -= 1
        
    for k, v in map.items():
        if v > 0:
            return k