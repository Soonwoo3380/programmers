def solution(dots):
    a, b, c, d = dots
    
    def solution_2(d1, d2, d3, d4):
        return (d1[1]-d2[1]) * (d3[0]-d4[0]) == (d1[0]-d2[0]) * (d3[1]-d4[1])
    
    if solution_2(a, b, c, d):
        return 1
    if solution_2(a, c, b, d):
        return 1
    if solution_2(a, d, b, d):
        return 1
    
    return 0