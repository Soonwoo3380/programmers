def solution(lines):
    answer = []
    list = []

    for line in lines:
        for num in range(line[0], line[1]):
            list.append((num, num+1))

    for i in range(len(list)):
        if list.count(list[i]) >= 2:
            answer.append(list[i])

    return len(set(answer))