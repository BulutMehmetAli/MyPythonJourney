def  minRemovals(array , target):

    if not array or target < 0:
        return False
    
    totalSum = sum(array)
    newValue = totalSum - target
    
    if newValue == 0:
        return 0 
    if newValue < 0:
        return -1 
    
    counter1 = 0
    
    for i in range(len(array)):
        # counter2 = 0
        currentSum = 0
        for j in range(i,len(array)):
            currentSum += array[j]
            # counter2 += 1
            if currentSum == newValue:
                counter1 = max(counter1 , j-i+1)
    if counter1 == 0:
        return -1
    return len(array) - counter1

array = [3, 4, 1, 3, 2 , 5]

print(minRemovals(array , 5))