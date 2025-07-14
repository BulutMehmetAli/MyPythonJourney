array = [1,1,2,1,1 ,1, 2,1, 2 , 5]

currentSum = 0
targetNumber = 6
left = 0
cuounter = 0
for i in range(len(array)):
    currentSum += array[i]
    
    
    while(currentSum > targetNumber):
        currentSum -= array[left]
        left += 1
    
    if currentSum == targetNumber:
        cuounter = max(cuounter , i - left +1)

print(cuounter)

    