def convertComplement(numb):
    stringNumber = 32*'0'
    
    n = 31
    k = -1
    while n >= 0:
        temp = pow(2 , n)
        k += 1
        if numb >= temp:
            stringNumber = stringNumber[:k] + "1" + stringNumber[k+1:]
            numb -= temp
        n -= 1
    return stringNumber

def complement(numb):
    temp = convertComplement(numb)   # binary string
    lst = list(temp)                 # string → liste
    for i in range(len(lst)):
        if lst[i] == '0':
            lst[i] = '1'
        else:
            lst[i] = '0'
    
    # return "".join(lst) 
    n = 31
    sum = 0
    for i in range(len(temp)):
        if lst[i] == '1':
            sum += pow(2 , n)
        n -= 1
    return sum 



print(complement(43261596))

