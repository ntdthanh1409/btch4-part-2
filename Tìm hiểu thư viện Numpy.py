import numpy as np
n = np.array([(4,5,6), (1,2,3)])
m = np.array([(3,5,6), (3,5,7)])
k = m + n
h = m * n
t = np.transpose(m)
print("Tổng của hai ma trận:",k)
print("Tích của hai ma trận:",h)
print("Ma trận chuyển vị của m là:",t)
