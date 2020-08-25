import numpy as np
import time

def shellSort(a):
    
    gap = int(len(a)/2)
    while gap > 0:

        for i in range(gap, len(a)):
            temp = a[i]
            j = i

            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j = j-gap
            a[j] = temp

        gap = int(gap/2)

start_time = time.time()
n = 50000
a = np.random.randint(500000, size = n)

shellSort(a)
print(a)
print("--- sorting cost %s seconds ---" % (time.time() - start_time))