import numpy as np

#Scalar arithmetic

arr = np.array([1,2,3])

#basic operations
print(arr + 1)
print(arr - 2)
print(arr * 2)
print(arr / 2)
print(arr** 2)



#Vectorized math func
print(np.sqrt(arr))
print(np.pow(arr,2))
print(np.round(arr))
print(np.floor(arr))
print(np.ceil(arr))
print(np.pi)


#=========================#
radii = np.array([1,2,3])

print(np.pi * radii ** 2)
#=========================#



#Element-wise arithmetic
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)




#Comparison operators
scores = np.array([91,55,100,73,82,64,14,25,36])
# print(scores)
scores[scores<60] = 0 #makes all scores which have value of less than 60 to have a value of 0. you can put print(scores) before 
#                                                                               and after that line to see the actual difference
# print(scores)

print(["passed" if score >= 60 else "did not pass" for score in scores])


print(scores < 60)