def constant_mult(arr1,arr2):
  product=[]
  temp=[]
  temp.append(arr1[0][0]*arr2[0][0]+arr1[0][1]*arr2[1][0])
  temp.append(arr1[0][0]*arr2[0][1]+arr1[0][1]*arr2[1][1])
  product.append(temp)
  temp=[]
  temp.append(arr1[1][0]*arr2[0][0]+arr1[1][1]*arr2[1][0])
  temp.append(arr1[1][0]*arr2[0][1]+arr1[1][1]*arr2[1][1])

A1=[
    [1,2,3,4],
    [4,5,6,7],
    [9,10,11,12],
    [6,4,3,2]
]
A2=[
    [4,6,7,8],
    [0,8,9,2],
    [1,2,3,4],
    [3,12,3,4]
]
constant_mult(A1)
