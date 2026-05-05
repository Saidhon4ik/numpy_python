import numpy as np
#=================================================================================#
rng = np.random.default_rng() 
#np.random.default_rng(seed = 1) seed keeps those random numbers, they wont change
#=================================================================================#



#================================================#
print(rng.integers(low = 1, high = 7,size=(3,2)))
#================================================#



#===============================================================================#
#floating point number. 
np.random.seed(seed = 1)
print(np.random.uniform(low=-1, high=1,size=(3,2))) #between 0 and 1 by default
#================================================================================#



#=============================#
#shuffle
arr = np.array([1,2,3,4,5])
rng.shuffle(arr)
print(arr)
#=============================#



#=============================================================#
#random choice
fruits = np.array(["apple","banana","coconut","kiwi"])
fruit = rng.choice(fruits,size = (3,2))
print(fruit)
# example output
# [['apple' 'banana']
#  ['apple' 'apple']
#  ['apple' 'apple']]
#=============================================================#