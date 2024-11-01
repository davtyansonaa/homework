def heapify(array, n , i):
  largest = i
  l = 2*i + 1
  r= 2*i + 2

  if l<n and array[i]<array[l]:
    largest = l
  if r<n and array[largest]<array[r]:
    largest = r
  if largest !=i:
    array[i], array[largest]=array[largest],array[i]
    heapify(array, n, largest)#check to see if after swap something changed in tree

def heapSort():
  array=[22,3,7,27,35,6,17,1]
  n = len(array)

  for i in range(n//2, -1, -1):
    heapify(array, n, i)
  print(array)
  for i in range(n-1, 0, -1):
    array[i], array[0] = array[0], array[i]
    heapify(array, i, 0)
  print(array)


heapSort()
