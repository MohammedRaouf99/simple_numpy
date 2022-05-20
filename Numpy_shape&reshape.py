import numpy as np

# #=====Shape=====#
array = np.array([1, 2, 3, 4])  # ==> 4 one dimension and one-four elemints
# print(array.ndim)
# print(array.shape)

# # ==> (2,4) two dimension and two-four elemints
# array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(array1.ndim)
# print(array1.shape)

# # ==> (2, 2, 2) three dimension and two-two-two
# array2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(array2.ndim)
# print(array2.shape)

#=====Reshape======#

reshape_array = array.reshape(2, 2)
print(reshape_array)  # [[1 ,2],[3 ,4]]
reshape_array = array.reshape(-1) # (-1)from Two dimension to One dimension 
print(reshape_array.ndim)  # [1 2 3 4]
