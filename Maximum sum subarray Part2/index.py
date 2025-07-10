def ourFunction(array, limit):
    if not array:
        return -1

    max_sum = 0
    n = len(array)
    current_sum = 0
    j = 0
    for i in range(n):
        current_sum += array[i]
        while current_sum > limit and j <= i:
            current_sum -= array[j]
            j += 1 
        max_sum = max(max_sum , current_sum)

    return max_sum

array = [8,2,12,6,5,8,13]
array.sort()

print(ourFunction(array , 15))
