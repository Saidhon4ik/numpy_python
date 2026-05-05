#========================================================================#
#Aggregate functions = summarize data and typically return a single value
#========================================================================#
import numpy as np

arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])

#===============================================#
#Basic ones
print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr)) #statistic thing
print(np.var(arr)) #statistic thing
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr)) #index of a minimum number
print(np.argmax(arr)) #index of a maxumum number
#================================================#

print(np.sum(arr,axis = 1)) #we are summing all columns | axis = 0 sum of all columns | axis = 1 sum of all rows