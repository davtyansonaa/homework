def multArr(arr1,arr2):
  sum0=0
  product=[]
  for i in range(len(arr1)):
    temp=[]
    for j in range(len(arr2[0])):
        for k in range(len(arr2[0])):
          sum0+=arr1[i][k]*arr2[k][j]
        temp.append(sum0)
        sum0=0
    product.append(temp)
  return product


A1=[[0,1,2],
    [3,5,7],
    [9,10,11]
    ]
A2=[
    [4,5,6],
    [7,8,9],
    [10,9,12]
]

print(multArr(A1,A2))
