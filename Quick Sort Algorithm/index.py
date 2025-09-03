def partition(arr , low , high):
    pivot = arr[high]
    i = low - 1
    for j in range(low , high):
        if arr[j] <=pivot:
            i+=1
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i+1] , arr[high] = arr[high] , arr[i+1]
    return i+1
    

def quickSort(arr , low , high):
# pi 'den kastımız pivot seçimidir.
    if low < high:
        pi = partition(arr , low , high)
        quickSort(arr , low , pi-1)
        quickSort(arr , pi+1 , high)
    



array = [25 , 10 , 5 , 30 , 40 , 2 , 1 , 18 , 7]
quickSort(array , 0 , len(array) - 1)
print(array)