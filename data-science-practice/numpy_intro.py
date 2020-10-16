
import numpy as np      # universal standard to abbreviate numpy as np

arr = np.array([1, 2, 3])   # numpy arrays are similar to python lists

print(arr) # [1, 2, 3]

print(type(arr[1])) # numpy.int32  (32 bits)
print(arr.dtype) #int32

# Datatypes can be altered:
arr64 = np.array([1, 2, 3], dtype=np.int64)

print(type(arr64[0])) # numpy.int64
print(arr.dtype) # int64
