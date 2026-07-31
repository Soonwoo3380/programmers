def solution(n, lost, reserve):
    students = [1] * n

    for idx in reserve:
        students[idx-1] += 1

    for idx in lost:
        students[idx-1] -= 1



    for i in range(n):
        if students[i] == 0:
            if i == 0 and n > 1:
                if students[1] == 2:
                    students[0] = 1
                    students[1] = 1
                else:
                    pass
            elif i != 0 and i != n-1:
                if students[i-1] == 2:
                    students[i] = 1
                    students[i-1] = 1
                elif students[i+1] == 2:
                    students[i] = 1
                    students[i+1] = 1
                else:
                    pass
            else:
                if students[i-1] == 2:
                    students[i] = 1
                    students[i-1] = 1
                else:
                    pass

        


    for j in range(n):
        if students[j] > 1:
            students[j] = 1
        else:
            pass


    return sum(students)