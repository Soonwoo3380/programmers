def solution(numlist, n):
    diff = []

    for num in numlist:
        diff.append(abs(n - num))
        
    for i in range(len(numlist)):
        swapped = False

        for j in range(0, len(numlist) - i - 1):
            if diff[j] > diff[j + 1]:
                diff[j], diff[j + 1] = diff[j + 1], diff[j]
                numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
                swapped = True

            elif diff[j] == diff[j + 1]:
                if numlist[j + 1] > numlist[j]:
                    numlist[j + 1], numlist[j] = numlist[j], numlist[j + 1]
                swapped = True

        if not swapped:
            break
            
    return numlist