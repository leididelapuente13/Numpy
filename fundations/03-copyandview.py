import numpy as np

# array copy - if the original array changes it does not affect the copy and the copy changes won't affect the original array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
arr_copy = arr.copy()
arr[0] = 42

# array view - the changes made in the original array will affect the view and the changes of the view will affect the original array
arr_view = arr.view()
arr[1] = 20
arr_view[2] = 22
print(arr, arr_view)

# how to check if an array owns its data? - the view will return the original and the copy base
print(arr








      .base)