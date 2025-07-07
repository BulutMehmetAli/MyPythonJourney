array = [1,3,-1,-3,5,3,6,7]

windowSize = int(input("Enter window size:"))
newArray = []
tempArray = []
for i in range(len(array)):
    tempArray.append(array[i])
    if(i >= windowSize-1):
        maxValue = max(tempArray)
        newArray.append(maxValue)
        tempArray.pop(0)
       

print(newArray)


# Alternatif çözüm

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, array, windowSize):
        if not array or windowSize == 0:
            return []

        q = deque()  
        newArray = []

        for i in range(len(array)):
           
            if q and q[0] <= i - windowSize:
                q.popleft()

            
            while q and array[q[-1]] < array[i]:
                q.pop()

            q.append(i)

            if i >= windowSize - 1:
                newArray.append(array[q[0]])

        return newArray
    
"""
Avantajlar:
✔ Büyük veri setinde hızlı çalışır
✔ Kaydırmalı pencere için endüstri standart çözüm
✔ En kötü senaryoda bile O(n) zaman
✔ Memory verimliliği yüksek
"""
