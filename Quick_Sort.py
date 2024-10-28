def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    index = arr[len(arr) // 2]  
    dzax = [x for x in arr if x < index]
    mijin = [x for x in arr if x == index]
    aj = [x for x in arr if x > index]
    return quick_sort(dzax) + mijin + quick_sort(aj)
