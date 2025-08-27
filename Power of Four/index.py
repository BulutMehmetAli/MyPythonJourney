def powerFour(value):
    if value == 0:
        return True
    temp = value // 4
    temp2 = 1
    while temp > 0:
        temp2 *= 4
        temp -= 1
        if temp2 == value:
            return True
    return False
    
while True:
    number = int(input("Enter number:"))
    print(powerFour(number))