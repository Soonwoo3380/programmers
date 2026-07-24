def solution(array):

    elements = list(set(array))
    counts = [0] * len(elements)

    for num in array:
        idx = elements.index(num)
        counts[idx] += 1

    max_n = 0
    max_idx = 0
    for j in range(len(counts)):
        if max_n < counts[j]:
            max_n = counts[j]
            max_idx = j

    mode = 0
    for k in range(len(counts)):
        if max_n == counts[k]:
            mode += 1
    if mode > 1:
        return -1
    else:
        return elements[max_idx]