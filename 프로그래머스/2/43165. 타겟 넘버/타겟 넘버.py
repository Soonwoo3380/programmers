def solution(numbers, target):
    def dfs(index, current):
        if index == len(numbers):
            if current == target:
                return 1
            return 0
        
        plus_c = dfs(index + 1, current + numbers[index])
        minus_c = dfs(index + 1, current - numbers[index])
        
        return plus_c + minus_c
    
    return dfs(0, 0)