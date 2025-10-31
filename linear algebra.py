#in class
import numpy as np
a = np.array([10, 20, 30, 40, 50])
b = np.array([7,5,4,3,9])
arr=np.dot(a,b)
print(arr)
#860

arr=np.inner(a,b)
print(arr)
#860

arr=np.outer(a,b)
print(arr)
#[[ 70  50  40  30  90]
#[140 100  80  60 180]
#[210 150 120  90 270]
#[280 200 160 120 360]
#[350 250 200 150 450]]
a = np.array([[10, 20],[42,52]])
lin=np.linalg.det(a)
print(lin)           #-319.999


#practice

# 1D dot product
a = np.array([1, 2, 3])        # Vector a
b = np.array([4, 5, 6])        # Vector b
print(np.dot(a, b))            # Dot = 1*4 + 2*5 + 3*6 = 32

# 2D dot product (Matrix multiplication)
A = np.array([[1, 2],
              [3, 4]])         # Matrix A
B = np.array([[5, 6],
              [7, 8]])         # Matrix B
print(np.dot(A, B))            # Matrix dot product

# 1D inner
print(np.inner(a, b))          # Similar to dot in 1D

# 2D inner
print(np.inner(A, B))          # Inner product between rows of matrices

# 1D outer
print(np.outer(a, b))          # Creates a matrix = each element cross multiplied

# 2D outer (matrix flattened to vector automatically)
print(np.outer(A, B))          # 4x4 matrix output

# Only for square matrix (2D)
print(np.linalg.inv(A))        # Inverse of matrix A

print(np.linalg.det(A))        # Determinant of matrix A

print(np.trace(A))             # trace = 1 + 4 = 5

M = np.array([[3, 1],
              [1, 2]])         # Matrix M
C = np.array([9, 8])           # Constant values B

print(np.linalg.solve(M, C))   # Solution of x such that Mx = C











