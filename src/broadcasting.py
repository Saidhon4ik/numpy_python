#===========================================================#
#Broadcasting allows NumPy to perform operations on arrays
#with different shapes and virtually expanding dimensions
#so they match larger array's shape


#The dimensions have the same size
#OR
#One of the dimensions has a size of 1


#(10,1) * (1,10)    --> 👍
#(10,10) * (10,1)   --> 👍
#(10,10) * (10,10 ) --> 👍
#===========================================================#



#================================#
import numpy as np
arr1 = np.array([[1],
                 [2],
                 [3],
                 [4]])
arr2 = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])
arr3 = np.array([[1,2,3,4]])
#================================#



#===========================#
#just checking their shapes
print(arr1.shape)
print(arr2.shape)
#===========================#


#===========================#
#mul
print(arr1 * arr2)
print(arr1 * arr3)
#===========================#



#=============================================#
array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],
                   [2],
                   [3],
                   [4],
                   [5],
                   [6],
                   [7],
                   [8],
                   [9],
                   [10],])
#=============================================#


#====================#
print(array1.shape)
print(array2.shape)
print(array1*array2)
#====================#