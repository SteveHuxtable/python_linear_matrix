import numpy as np

test_data = [1, 2, 3, 4, 5]
test_arr = np.array(test_data)
test_arr.dtype

test_data2 = [[1, 2, 3], [1.0, 2.0, 3.0]]
test_arr2 = np.array(test_data2)
test_arr2.dtype

np.empty((2, 3, 2))
np.arange(15)
np.arange(2, 100, 2)
range(2, 50, 2)
 for i in range(2, 50, 2):
     print(i)
     print('\n')

np.identity(10)

test_arr3 = np.array([1 , 2, 3], dtype=np.float64)
test_arr3 = test_arr3.astype(np.int32)

test_arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr_pointer = test_arr4[2:4]
arr_pointer[0] = 999

test_arr4[~(test_arr4 > 100)]

test_arr5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = np.array([True, False, True])
test_arr5[mask, 1]

# create a matrix
test_arr6 = np.empty((4, 4))
for i in range(4):
    for j in range(4):
        test_arr6[i, j] = i * j

test_arr7 = np.arange(56).reshape((8, 7))
test_arr7[[1, 2, 3], 2]

test_arr7.T.dot(test_arr7)
np.dot(test_arr7.T, test_arr7)

points = np.arange(-5, 5, 0.01)

xs, ys = np.meshgrid(points, points)

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

cond_arr = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
# a tidy version
cond_arr2 = np.where(cond, xarr, yarr)

arr = np.random.randn(5, 4)
arr.mean()
arr.mean(axis=1)
arr.mean(axis=0)

arr = np.random.randn(100)
(arr > 0).sum()

arr = np.arange(10)