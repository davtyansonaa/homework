def mergeSort(arr):

  if len(arr)<=1:
    return arr

  n=len(arr)//2
  left_half=arr[ :n]
  right_half=arr[n: ]

  sorted_left=mergeSort(left_half)
  sorted_right=mergeSort(right_half)

  return merge(sorted_left,sorted_right)

def merge(left,right):

  result=[]
  i=j=0

  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      result.append(left[i])
      i+=1
    else:
      result.append(right[j])
      j+=1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

unsorted_arr=[5,8,14,7,19,6,1,99]
sorted=mergeSort(unsorted_arr)
print(sorted)
