import numpy

# how to set a type for the data in the array
array = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], dtype='i')
array_1 = numpy.array(["banana", "cherry", "strawberry", "apple"], dtype='S')

# how to know the type of the data in the array?
print(array_1.dtype)

# how to convert the data inside the array to other type?
old_array = numpy.array([1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0])
new_array = old_array.astype('i')

# --- numpy types ---
# i - integer
# b - boolean
# f - float
# c - complex float
# M - datetime
# O - object
# S - string