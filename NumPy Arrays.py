import numpy as np

arr_1d = np.arange(1, 13)
arr_2d = arr_1d.reshape(3, 4)

print("Original 3x4 Array:\n", arr_2d)
print("\nElement at Row 1, Column 2:", arr_2d[1, 2])
print("Last row:", arr_2d[-1])
print("\nFirst two rows, columns 1 to 3:\n", arr_2d[0:2, 1:3])
print("\nEvery alternate column:\n", arr_2d[:, ::2])

arr_3d = arr_2d.reshape(2, 2, 3)
print("\nReshaped to 3D (2x2x3):\n", arr_3d)
print("\nFlattened Array:", arr_2d.flatten())
print("Column-wise Sum:", np.sum(arr_2d, axis=0))
print("Row-wise Maximum:", np.max(arr_2d, axis=1))