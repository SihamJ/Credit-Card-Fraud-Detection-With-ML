import numpy as np
import time


## LIST
a = [i for i in range(10000000)]
b = [i for i in range(10000000)]

t1 = time.time()
for i in range(len(a)):
    c = a[i] * b[i]
t1 = time.time() - t1

print("\nMultiplication Time List: " +str(t1) + ' s\n')

## NUMPY
aa = np.array(a)
bb = np.array(b)

t1 = time.time()
cc = aa * bb 
t1 = time.time() - t1

print("Multiplication Time NumPy: " +str(t1) + ' s\n')