def solution(park, routes):
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                x, y = i, j
                
    direction = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }
    
    for route in routes:
        d, n = route.split()
        n = int(n)
        
        dx, dy = direction[d]
        
        nx, ny = x, y
        
        for _ in range(n):
            nx += dx
            ny += dy
            
            if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]):
                break
                
            if park[nx][ny] == "X":
                break
                
        else:
            x, y = nx, ny
            
    return [x, y]
                