def findSub(array):
    n = len(array)
    counter = 0
    for i in range(n):
        for j in range(i+1 , n):
            if(array[j] > array[j-1]):
                counter += 1
            else:
                break
    return counter


array = [2,2,2,2,2]
print(findSub(array))