def solution(priorities, location):
    answer = 0
    index = 0

    while True:
        if priorities[index] == max(priorities):
            answer += 1

            if index == location:
                return answer

            priorities[index] = 0

        index = (index + 1) % len(priorities)
    
    