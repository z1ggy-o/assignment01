import numpy as np

def f_i(x, i):
    return x[i]

def create_A(func, data, num_data, size):
    A = []
    
    for i in range(num_data):
        img = data[:, i]  # ith image(column)
        row = [func(img, j) for j in range(size)]
        A.append(row)
    
    return np.array(A)

list = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

data = np.array(list)

m = create_A(f_i, data, 3, 3)

print(m)