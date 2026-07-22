def solution(array, commands):

    answer = []

    for command in commands:

        i, j, k = command[0], command[1], command[2]
        a_part_of_list = array[i-1:j]

        for step in range(len(a_part_of_list)):
            min_index = step

            for index in range(step+1, len(a_part_of_list)):
                if a_part_of_list[index] < a_part_of_list[min_index]:
                    min_index = index

            a_part_of_list[step], a_part_of_list[min_index] = a_part_of_list[min_index], a_part_of_list[step]

        answer.append(a_part_of_list[k-1])

    return answer    