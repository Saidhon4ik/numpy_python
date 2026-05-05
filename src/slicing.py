#Slicing in numpy
import numpy as np


arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]
                ])



#print(arr[i,j]) where i is a row and j is a column



#=====================#
#array[start:end:step]
print(arr[0::2])
#=====================#



#==============================================================================#
#So, basically that thing gives us all rows, but the 'n' th column of each one.
print(arr[:,0])
#==============================================================================#



#=======================================================================#
#this one tho gives us all rows but in the range from n-n to n th column
print(arr[:, 1:4])
#=======================================================================#



#=================================================#
#this one outputs every second column in all rows
print(arr[:, ::2])
#=================================================#



#===========================================================#
#selects the first two rows' two first columns in those rows
print(arr[0:2,0:2])
#===========================================================#