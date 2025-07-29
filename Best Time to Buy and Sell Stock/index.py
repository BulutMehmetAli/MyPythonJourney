def calcPriceMax(arr):

    arrSize = len(arr)
    j = arrSize - 1
    maxValue = -2**31  # Eğer 32-bit int sınırı kullanıyorsan
    i = 0
    while(i<j):
        if arr[i] > arr[j]:
            i += 1
        elif arr[j] > arr[i]:
            value = arr[j] - arr[i]
            maxValue = max(maxValue ,value)
            j -= 1 


    if maxValue > 0:
        return maxValue
    else:
        return 0

prices =[7,1,5,3,6,4]


print(calcPriceMax(prices))


"""

Alternative Solution

class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price 
            elif price - min_price > max_profit:
                max_profit = price - min_price 

        return max_profit
prices =[7,1,5,3,6,4]


"""