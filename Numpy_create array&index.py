# # import module Numpy
import numpy as np

# create array with Numpy
x = np.array(10)  # zero dimension array
print(x)
print(x.ndim)  # how to know number of dimension

y = np.array([1, 2, 3, 4, 5])  # one dimension array
print(y)
print(y.ndim)

z = np.array([[1, 3], [5, 9]])  # two dimensions array
print(z)
print(z.ndim)

s = np.array([[[1, 2]]])
print(s)
print(s.ndim)

#====================================================#

# index array

a = np.array([[[1, 2], [3, 5]], [[4, 7], [8, 5]]])
print(a[0][0][1])  # output ===> 2
print(a[0, 1, 1])   # output ===> 5

# slicing array

v = np.array([[["a", "b", "c"], ["d", "f", "g"]], [["h", "j", "k"], ["l", "z", "x"]]])  # three dimension
print(v[1])
print(v[1:, 0, 1])  # ===> ["j"]


m = np.array([["a", "b", "c"], ["d", "f", "g"], ["h", "j", "k"], ["l", "z", "x"]])  # two dimension
print(m[1:, 0:2])
