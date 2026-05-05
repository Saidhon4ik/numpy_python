#===============================================================================#
#Filtering in numpy = Refers to the proccess of selecting elements from an array
#that matches given condition
#Sort of a 'Where' thing from SQL but in numpy python
#===============================================================================#
import numpy as np

ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,19,20,21]])



#======================================#
#our arrays
teens = ages[ages < 18]
adults1 = ages[(ages<=18) & (ages<65)]
seniors = ages[ages>=65]
evens = ages[ages%2 == 0]
odds = ages[ages%2 != 0]
#======================================#



#==============#
#calling all functions
print(teens)
print(adults1)
print(seniors)
print(evens)
print(odds)
#==============#



#=================================================================================================#
#you use where only to keep your array's dimension, but it is much slower than previous versions
adults = np.where(ages>=18,ages,np.nan)
print(adults)
#=================================================================================================#