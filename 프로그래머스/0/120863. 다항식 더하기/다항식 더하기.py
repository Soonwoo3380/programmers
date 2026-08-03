def solution(polynomial):
    polynomial_list = []

    for elem in polynomial.split(' + '):
        polynomial_list.append(elem)

    answer_for_x_arguments = 0
    constant = 0

    for item in polynomial_list:
        if 'x' in item:
            if item == 'x':
                answer_for_x_arguments += 1
            else:
                answer_for_x_arguments += int(item.replace('x', ''))
        else:
            constant += int(item)

    answer = 0
    if constant == 0:
        if answer_for_x_arguments != 1:
            answer = f'{answer_for_x_arguments}x'
        else:
            answer = 'x'
    elif answer_for_x_arguments == 0:
        answer = f'{constant}'
    else:
        if answer_for_x_arguments != 1: 
            answer = f'{answer_for_x_arguments}x + {constant}'
        else:
            answer = f'x + {constant}'

    return answer