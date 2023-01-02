import numpy as np
"""Basics of Numpy"""
# a = np.array([1,2,3]) #1-D Array
# print(a) #[1 2 3]

# b = np.array([[1,2,3,4,5],[6,7,8,9,10]]) #2-D Array
# print(b) #[ 1  2  3  4  5]
#         #[ 6  7  8  9 10]]
# print(a.ndim)# Dimension for a
# print(b.ndim)# Dimension for b

# print(a.shape) # Rows,Colunms for the Array a
# print(b.shape) # Rows,Colunms for the Array b

# print(a.dtype) # type of data (Can be specified before also)
# print(b.dtype) 

# c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]], dtype='int16') # Specified Data type
# d = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]], dtype='int32')

# print(c[1,3]) # 2nd row 4th column (starts from 0)
# print(c[1, :]) # all elements in the 2nd row

# print(c[0,1:6:2]) # startindex:endindex:stepsize

"""Building Matrices in NUMPY"""
# e = np.zeros((2,3)) #makes a zero matrix with rows and columns
# print(e)

# f = np.ones((3,4)) #makes a ones matrix with rows and columns 
# print(f)

# g = np.full((2,3),5) # makes a matrix with input variable
# print(g)

# h = np.random.randint(-5,8, size=(2,3)) #randoms values array between selected parameters
# print(h)

# i = np.identity(6) #identity matrix for parameter.
# print(i)

# j = np.array([1,2,3])
# j1 = np.repeat(j,2,axis=0) #repeats the element as parameter
# print(j1)

"""Mathematics in NUMPY"""

# k = np.array([1,2,3,4,5]) #Mathematical operations happens on all elements
# print(k+2)
# print(k-2)
# print(k*2)
# print(k/2)
# print(k**2)

# l = np.array([1,2,3,4,5]) #Trigonometric Functions also aplly on all elements
# print(np.cos(l))
# print(np.sin(l))
# print(np.tan(l))

"""Linear Algebra"""

# m = np.array([[1,2,3,4],[5,6,7,8]])
# n = np.array([5,6,7,8]) #Performs Corresponding element operations

# print(m+n) 
# print(m*n)
# print(m-n)
# print(m/n)

# o = np.ones((4,2))
# print(np.matmul(m,o)) #Performs Matrix Multiplication..
# p = np.identity(4)
# print(np.linalg.det(p))# Finds determinant of the matrix

"""
Some other operations in Linear Algebra
1.Trace
2.Singular Vector Decompostion
3.Eigenvalues
4.Matrix Norms
5.Inverse
"""

"""Statistics"""

# stats = np.array([[1,2,3,4],[5,6,7,8]])
# print(np.min(stats)) # Maximum and Minimum of Array
# print(np.max(stats))

# print(np.sum(stats)) # Sum of all elements.

# v1 = np.array([[1,2,3,4],[5,6,7,8]])
# v2 = np.array([[9,10,11,12],[13,14,15,16]])

# print(np.vstack(v1,v2)) # Vertically stacks two arrays
# print(np.hstack(v1,v2)) # Horizontal stacks two arrays

""" Loading data from files """
x = np.genfromtxt('n1.txt',delimiter=',')
print(x)








