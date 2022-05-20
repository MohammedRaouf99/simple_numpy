# import module
import numpy as np

#=========One Dimension===========#

# sum
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
# you must be same shape
print(array1 + array2)

# sub

print(array1 - array2)

# mult

print(array1 * array2)

#  div

print(array1 / array2)

#=============Two Dimension=========#

array3 = np.array([[10, 20], [40, 50]])
array4 = np.array([[30, 60], [70, 10]])

# sum
print(array3 + array4)

# sub
print(array3 - array4)

# mult

print(array3 * array4)

# div

print(array3 / array4)
