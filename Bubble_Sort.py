def bubble_sort(arr):
  for _ in range(len(arr)):
    for i in range(len(arr)-1):
      if arr[i]>arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]
  return arr
arr=[1,4,5,7,8,20,1,56,112,3]
print(bubble_sort(arr))
