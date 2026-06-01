# NumPy Syntax Cheatsheet 📝

| Signature | Description | Tiny Example |
| :--- | :--- | :--- |
| `np.array(list)` | Creates an array from a list | `np.array([1, 2, 3])` |
| `np.zeros(shape)` | Creates an array of zeros | `np.zeros((2, 2))` |
| `np.ones(shape)` | Creates an array of ones | `np.ones((3, 1))` |
| `np.arange(start, stop, step)` | Returns evenly spaced values | `np.arange(0, 10, 2)` |
| `np.linspace(start, stop, num)` | Returns `num` points between start/stop | `np.linspace(0, 1, 5)` |
| `arr.shape` | Returns the dimensions of the array | `arr.shape` |
| `arr.reshape(new_shape)` | Changes the shape without changing data | `arr.reshape(5, 2)` |
| `arr.dtype` | Returns the data type of elements | `arr.dtype` |
| `np.dot(a, b)` | Dot product of two arrays | `np.dot(a, b)` |
| `arr.sum(axis)` | Sum of array elements along an axis | `arr.sum(axis=0)` |
| `arr.mean()` | Compute the arithmetic mean | `arr.mean()` |
| `np.max(arr)` | Return the maximum of an array | `np.max(arr)` |
| `np.sqrt(arr)` | Square root of every element | `np.sqrt(arr)` |
| `arr[index]` | Accessing elements (0-indexed) | `arr[0, 1]` |
| `arr > val` | Boolean masking/filtering | `arr[arr > 5]` |
