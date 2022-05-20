from array import array
import numpy as np 

#========dtype========# 
array1 = np.array([1,2,3,4,5])
print(array1.dtype)  # int32

array2 = np.array([1.2,3.5,6.1])
print(array2.dtype)  # float64

array3 = np.array([1, 2, 3, "4", "5"])  # conver number to string
print(array3.dtype)  # <U11

array4 = np.array([1,2,3,"a","b" , True])   #conver number to string and True to string 
print(array4.dtype)  # <U11

array5 = np.array([1,2,3, True])  # convert True to 1 and False to 0
print(array5.dtype)  # int32


#========zeros========# 
array6 = np.zeros((3,4))  # 3 is Row and 4 is colum
print(array6)  # [[0. 0. 0. 0.][0. 0. 0. 0.][0. 0. 0. 0.]]


#========Ones=========# 
array7 = np.ones((3, 4))  # 3 is Row and 4 is colum
print(array7)  # [[1. 1. 1. 1.][1. 1. 1. 1.][1. 1. 1. 1.]]

#=======empty=========#
array8 = np.empty((2,3))
print(array8)

# #=======Range=========# 
array9 = np.arange(2,6) # get start and end (end is not included) and step  
print(array9)  # [2 3 4 5] 

array_9 = np.arange(2,6)**2
print(array_9)  # [ 4  9 16 25]
#======linspace=======#
array10 = np.linspace(0,3,3) # start and end and number of item in range 
print(array10)  # [0.  1.5 3. ]

#=======sum===========#
array11 = np.array([1,2,3,4,5])
print(array11.sum()) # 15 ===> sum of all item in array

array_11 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(array_11.sum(axis=1)) # 40 ===> sum of as Row 
#=======min===========#
array12 = np.array([1,2,3,4,5])
print(array12.min()) # 1 ===> return a minmaized value in array 

array_12 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array_12.min(axis=1))  # [1 6] min in single Row

#=========max===========#
array13 = np.array([1, 2, 3, 4, 5])
print(array13.max()) # 5 ===> return a maxmiam value in array

array_13 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(array_13.max(axis=1))  # [ 5 10] max in single Row
