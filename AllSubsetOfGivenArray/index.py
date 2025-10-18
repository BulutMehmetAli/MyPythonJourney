def subsets(nums):
    result = []

    def backtrack(start, current):
        
        result.append(current[:])

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            popped = current.pop()
            
    backtrack(0, [])
    return result


nums = [1, 2, 3]
result = subsets(nums)
print("\nAll  subsets:")
print(result)

