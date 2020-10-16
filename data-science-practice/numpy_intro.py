
import numpy as np      # universal standard to abbreviate numpy as np

# numpy arrays are similar to python lists
arr = np.array([1, 2, 3])   

print(arr) # [1, 2, 3]

print(type(arr[1])) # numpy.int32  (32 bits)
print(arr.dtype) #int32

# Datatypes can be altered:
arr64 = np.array([1, 2, 3], dtype=np.int64)

print(type(arr64[0])) # numpy.int64
print(arr.dtype) # int64

# you can multiply arrays using numpy
print(np.array([1, 2, 3]) * np.array([1, 2, 3])) 

# a matrix is a 2D array
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
matpy = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(mat) # prints an array per row
print(matpy) # prints out all lists in one row

# use of random in NumPy
v1 = np.random.rand(2) # an array of 2 random floating point numbers

print(v1)

# -------------
# arange
v = np.arange(12) # an array of nat up to 12
print(v)

# reshape reshapes given array into r rows and c columns
# reshape:         r  c 
v_mat = v.reshape((4, 3)) # reshapes v into a 4 row and 3 column matrix
print(v_mat)

# could be done in one line:
v_mat_new = np.arange(12).reshape((4, 3))
print(v_mat_new)

# the shape of an array i.e. (r, c) can be extracted using .shape method
print(v_mat.shape == v_mat_new.shape) # True

