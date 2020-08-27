import numpy as np
import time


def BubbleSort(a):
    n = len(a)
    for j in range(n-1):
        for i in range(n-j-1):
            if a[i] > a[i+1]:
                (a[i], a[i+1]) = (a[i+1], a[i])
            # else: continue
    return a


n = 5000
a = np.random.randint(500000, size=n)
start_time = time.time()
a = BubbleSort(a)
print(a)
print("--- sorting cost %s seconds ---" % (time.time() - start_time))
