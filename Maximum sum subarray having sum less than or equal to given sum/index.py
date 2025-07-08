# def slidingWindow(array,windowSize):

#     if not array or windowSize < 0:
#         return -1

#     maxValue = array[0]
#     sum = 0

#     for i in range(len(array)):
#         sum += array[i]
#         if(i>=windowSize-1):
#             maxValue = max(maxValue , sum)
#             sum -= array[i - windowSize + 1]
#     return maxValue

def ourFunction(array , limit):
    if not array:
        return -1
    sum = 0  
    n = len(array)
    for i in range(n):
        currentSum = 0
        for j in range(i , n):
            currentSum += array[j]
            if(currentSum < limit):
                sum = max(sum,currentSum)
            else:
                break
    return sum
   

   
# windowSize = int(input("Enter window size:"))
array = [8,2,12,6,5,8,13]
array.sort()

print(ourFunction(array , 25))

# 2 , 5 , 6 , 8 , 8 , 12 , 13