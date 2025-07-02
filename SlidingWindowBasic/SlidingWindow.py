array = [100, 200, 300, 400]
windowSize = int(input("Enter window size: "))

maxValue = 0
currentSum = 0

for i in range(len(array)):
    currentSum += array[i]

    if i >= windowSize - 1:
        maxValue = max(maxValue, currentSum)
        currentSum -= array[i - windowSize + 1]

print(maxValue)

