import numpy as np
#=======for loop=======#
x = np.arange(1,101).reshape(10,10) * 2
for i in x :
    # print(i)
    pass
print(x.ndim)
print(x.reshape(-1).ndim)
#=======add=======#
# z = np.arange(1, 6)
# b = np.arange(1, 6)

# print(np.add(z,b))

