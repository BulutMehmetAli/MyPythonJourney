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


s = "545019895926555011334355552"

print(findSmallest(s))