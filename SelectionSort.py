import numpy as np
import time

def SelectionSort(a, n):
    
    for i in range(n-1):
        value = a[i]
        index = i
        for j in range (i+1, n):
            if (a[index] > a[j]):
                index = j

        if (i != index):
            (a[i], a[index]) = (a[index], a[i])
    return a

n = 50000
a = np.random.randint(500000,size=n)


start_time = time.time()

a = SelectionSort(a,n)
print(a)

print("--- sorting cost %s seconds ---" % (time.time() - start_time))