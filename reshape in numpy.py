import numpy as np 
arr=np.array([1,2,3,4])
num=arr.reshape(2,2)
num=arr.reshape(3,3)
num=arr.reshape(2,1,2)     # [[[1 2]]
                              # [[3 4]]]
num=arr.reshape(2,1,-2)   
num=arr.reshape(1,1) 
num=arr.reshape(4) 
arr.resize(2,2)           
print(arr)

arr.resize(2,1,2) 
print(arr)

arr.resize(2,-1,-2) 
print(arr)


arr.arange(3)
print(arr)

a=np.array([1,2,4])
b=np.array([3,5,6])
num=np.stack((a,b),axis=0)
print(num)
num1=np.stack((a,b),axis=1)
print(num1)


a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
num=np.stack((a,b),axis=1)
print(num)                                                                            
#output
# [[[ 1  2  3]
#   [ 7  8  9]]

#  [[ 4  5  6]
#   [10 11 12]]]

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
num=np.stack((a,b),axis=2)
print(num) 

#  [[[ 1  7]
#   [ 2  8]
#   [ 3  9]]

#  [[ 4 10]
#   [ 5 11]
#   [ 6 12]]]   

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
c=np.array([[13,14,15],[16,17,18]])
num=np.stack((a,b,c),axis=1)
print(num)
# [[[ 1  2  3]
#   [ 7  8  9]
#   [13 14 15]]

#  [[ 4  5  6]
#   [10 11 12]
#   [16 17 18]]]

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
c=np.array([[13,14,15],[16,17,18]])
num=np.stack((a,b,c),axis=2)
print(num)
# [[[ 1  7 13]
#   [ 2  8 14]
#   [ 3  9 15]]

#  [[ 4 10 16]
#   [ 5 11 17]
#   [ 6 12 18]]]

