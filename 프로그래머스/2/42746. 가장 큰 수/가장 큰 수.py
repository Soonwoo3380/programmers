def solution(numbers):
    str_numbers = [str(word) for word in numbers]

    def quick_sort(array):
        if len(array) <= 1:
            return array

        pivot = array[len(array) // 2]

        greater = [x for x in array if (x * 3) > (pivot * 3)]
        equal =     [x for x in array if (x * 3) == (pivot * 3)]
        less = [x for x in array if (x * 3) < (pivot * 3)]

        return quick_sort(greater) + equal + quick_sort(less)

    sorted_arr = quick_sort(str_numbers)
    result = "".join(sorted_arr)

    if result == '' or result[0] == '0':
        return '0'

    return result