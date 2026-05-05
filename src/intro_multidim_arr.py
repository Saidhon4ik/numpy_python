# #Introduction
# import numpy as np

# arr = np.array([1,2,3,4])

# arr = arr * 2

# print(arr)




#######Multidimensional arrays
import numpy as np

#zero dimensional array
arr = np.array([[['A','B','C'], ['D','E','F'], ['G','H','I']],
               [['J','K','L'], ['M','N','O'], ['P','Q','Q']],
               [['S','T','U'], ['V','W','X'], ['Y','Z','_']]])

# #number of dimensions
# print(arr.ndim)
# print(arr.shape) # outout is a tuple which consists of (depth, num of rows, num of columns)


# #it is chain indexing
# print(arr[0][0][1])



# #It is Multidimensional indexing. It is faster than chain indexing btw
# print(arr[0,0,0])



P = arr[1,2,0]
O = arr[1,1,2]
T = arr[2,0,1]
A = arr[0,0,0]
word = P+O+T+A+T+O
print(word.lower())