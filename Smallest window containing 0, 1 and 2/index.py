import sys
def findSmallest(s):
    last_seen = {'0':-1 , '1':-1 , '2':-1}
    rmin = sys.maxsize

    for i in range(len(s)):
        
        if s[i] in last_seen:
            last_seen[s[i]] = i
        
        if -1 not in last_seen.values():
            currentMin = min(last_seen.values())
            currentMax = max(last_seen.values())
            rmin = min(rmin ,  currentMax - currentMin + 1)
    
    return rmin if rmin != sys.maxsize else -1


s = "5450198295926555334355552"

print(findSmallest(s))

# Implement sliding window

import sys
def findSmallest(s):
    myArray = {'0':0 , '1':0 , '2':0}
    rmin = sys.maxsize
    left = 0
    for i in range(len(s)):

        if s[i] in myArray:
            myArray[s[i]] += 1

        while all(myArray[c] > 0 for c in myArray):
            rmin = min(rmin , i - left + 1)

            if s[left] in myArray:
                myArray[s[i]] -= 1
            left += 1
                 
        
    return rmin if rmin != sys.maxsize else -1

s = "5450198295926555334355552"

print(findSmallest(s))

    
