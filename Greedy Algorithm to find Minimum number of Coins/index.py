def findMin(values , dest):
    result = []
    values.sort(reverse=True)

    for coin in values:
        while dest>=coin:
            result.append(coin)
            dest-=coin
    return result

x = int(input("X:"))
values = [1,2,5,10]

result = findMin(values , x )

print(result)
