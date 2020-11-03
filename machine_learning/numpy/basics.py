import numpy as np
a = np.array([1, 2, 3])
print(a)
print(a.shape) # tuple of ndim elements
print(a.dtype) # data types
print(a.ndim) # number of dimensions
print(a.size) # total number of elements
print(a.itemsize) # return size of each elements in bytes

b = a * np.array([2, 0, 2]) # element wise multiplication
c = a + np.array([4, 2, 3]) # element wise summation
print(b)

print(type(b))

# dot product
l1 = np.array([1, 2, 3])
l2 = np.array([4, 5, 6])
dot = np.dot(l1, l2) # dot = l1 @ l2
print(dot)

# boolean indexing
bool_arr = a > 1
print(bool_arr, a[bool_arr]) # a[bool_arr] will have rank 1
b = np.where(a > 1, a, -1)
print(b)

# fancy indexing
a = np.array([10, 19, 30, 41, 50, 61])
idx = [1, 3, 5]
print(a[idx])

even_idx = np.argwhere(a % 2 == 0).flatten()
print(a[even_idx])

a = np.arange(1, 7)
print(a, a.shape)
b = a[:, np.newaxis]
print(b)
b = a[np.newaxis, :]
print(b)

# concatenation
print('Concatenation')
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
c = np.concatenate((a, b))
print(c)
c = np.concatenate((a, b), axis = 0)
print(c)
c = np.concatenate((a, b), axis = None)
print(c)

# hstack, vstack to concatenate horizontaly or verticaly.

# generate arrays
a = np.zeros((2, 3)) # deefault data types float64
a = np.ones((2, 3))
a = np.eye(3)
a = np.full((2, 3), 5.0)
print(a)
a = np.linspace(0, 10, 5)
print(a)
a = np.random.random((3, 2)) # unifor distribution
print(a)
a = np.random.randn(2, 3) # gaussian or normal distribution, mean = 0, var = 1

a = np.random.randint(2, 10, size = (2, 2))
a = np.random.choice([-2, -1, 5], size = 5)
print(a)

# linalg
a = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(a)
print(eigenvalues)
print(eigenvectors) #column vector
# e_vec * e_val = A * e_vec
b = eigenvectors[:, 0] * eigenvalues[0]
c = a @ eigenvectors[:, 0]
print(b == c)
print(np.allclose(b, c))