arr = [1,5,4,-2,8]

def bubbleSort(arr):
    size = len(arr)

    for i in range(size):
        for j in range(size-1):
            if arr[j+1]< arr[j]:      
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print(bubbleSort(arr))
# Kodun optimize edilmiş hali
# In place sorting yaptık. Ekstra liste oluşturmadık bundan dolayı O(1) Space complexity
arr = [1,5,4,-2,8]

def bubbleSort2(arr):
    size = len(arr)

    for i in range(size):
        swapped = False
        for j in range(size-1-i):
            if arr[j+1]< arr[j]:      
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr

print(bubbleSort(arr))