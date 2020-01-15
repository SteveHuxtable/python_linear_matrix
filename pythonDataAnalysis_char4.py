import numpy as np

data = [[1, 2, 3], [4, 5, 6]]
data = np.array(data)
print(data.shape)
print(data.dtype)
print(data.ndim)

print(np.zeros(10))
print(np.zeros((3, 6))
print(np.empty((2, 5)))

print(np.arange(15))
print(range(15))

for i in range(15):
    print(i) # this is right!

test_list = [1.0, 2.0, 3.0, 4.0, 5.0]
test_np_array = np.array(test_list)
print(test_np_array)
print(type(test_np_array))
print(test_np_array)

test_tuple = (1.0, 2.0, 3.0, 4.0)
print(test_tuple[1])
test_list[1] = 2.5
print(test_list)
test_tuple[1] = 2.5

# other ways to create a np.array
test_list = [[1, 2, 3], [4, 5, 6]]
test_np_ndarray = np.asarray(test_list)
print(test_np_ndarray)
print(type(test_np_ndarray))

test_one_array = np.ones_like(test_list)
test_zero_array = np.zeros_like(test_list)
print(test_one_array)
print(test_zero_array)
print(type(test_one_array))

test_identity_matrix = np.eye(10)
print(test_identity_matrix)

print(test_identity_matrix.dtype)
test_identity_matrix = np.asarray(test_identity_matrix, dtype = np.int32)
print(test_identity_matrix)
test_identity_matrix = test_identity_matrix.astype(np.float64)
print(test_identity_matrix)

test_list = [1, 2, 3, 4]
np_list = np.array(test_list)
np_list.astype(np.float64)
print(np_list)
np_list_2 = np_list.astype(np.float64)
print(np_list_2)

# slice
arr = np.arange(10)
arr_slice = arr[5:8]  # arr_slice is not a copy from arr! should pay attention
arr_slice[1] = 12345

# how to create a copy?
arr_copy = arr[5:8].copy()
arr_copy[0] = 999
print(arr)

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(names)
data = np.random.randn(7, 4)
data_2 = np.random.randn(10)
print(data)
print(data_2)

print(names == "Bob")
print(data[names == 'Bob'])
print(data[names != 'Bob'])
print(data[~(names == 'Bob')])
print(data[np.logical_not(names == 'Bob')])

# fancy indexing: 20200114
import numpy as np
arr = np.empty((8, 4))
print(arr)

for i in range(8):
    arr[i] = i

print(arr)

print(arr[1])
print(arr[1][2])
print(arr[1, 2])
print(arr[[1, 2, 3]])
print(arr[[1, 2, 3], 2])

arr = np.arange(32)
type(arr)
arr = arr.reshape((8, 4))
print(arr)
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])

# a much better version
print(arr[np.ix_([1, 5, 7, 2],[0, 3, 1, 2])])

# transpose
arr = np.random.randn(6, 3)
print(arr.T)
print(np.dot(arr.T, arr))

arr = np.arange(16).reshape((2, 2, 4))

# ufunc of numpy
arr = np.arange(10)
print(np.sqrt(arr))