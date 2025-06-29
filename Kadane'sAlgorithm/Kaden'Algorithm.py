array = [-2,1,-3,4,-1,2,1,-5,4]

current = array[0]
maxValue = array[0]

for i in range(1,len(array)):
    current += array[i]
    if(array[i]>=current):
        current = array[i]
    
    maxValue = max(maxValue , current)
print(maxValue)
