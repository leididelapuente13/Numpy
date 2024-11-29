import numpy

# create a one dimensional array
arr = numpy.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr)
print(type(arr))

# create a zero dimensional array
newArr = numpy.array(45)

# create two dimensional array
two_array = numpy.array([[1, 2, 3], [4, 5, 6]])

for element in two_array:
    print(element)

# how to know the dimensions of an array
print('array dimensions: ', arr.ndim)

# array indexing
print(two_array[1][0])

# how to slice an array? you pass the starting position and the end position
print(arr[0:4])

# slices from position 2 to the end of the array
print(arr[2:])

# slices from the start until the position is 4 position
print(arr[:4])

# slice steps
print(arr[1:8:2])
print(arr[::2])
print(two_array[0, 0::2])

arr = numpy.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
dimentions = arr.shape
arr1 = dimentions[0]
arr2 = dimentions[1]
arr3 = dimentions[2]

#for array1 in range(arr1):
#    for array2 in range(arr2):
#       for array3 in range(arr3):
#            print('matriz: ', arr[array1][array2][array3])
