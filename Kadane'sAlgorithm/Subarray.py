array = [2, 3, -8, 7, -1, 2, 3]

en_buyuk = array[0]
for i in range(len(array)):
    result = 0

    for j in range(i,len(array)):
        result += array[j]
        en_buyuk = max(en_buyuk , result)

print(en_buyuk)
