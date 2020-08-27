import numpy as np
import time


def insertionSort(a, n):
    for i in range(n):
        index = i
        value = a[i]
        while (index > 0 and a[index - 1] > value):
            a[index] = a[index - 1]
            index -= 1
        a[index] = value
    return a

n = 50000
a = np.random.randint(500000, size = n)    

start_time = time.time()
insertionSort(a, n)
print(a)
print("--- sorting cost %s seconds ---" % (time.time() - start_time))