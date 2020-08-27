import numpy as np
import time

def partition(a, l, h):
    pivot = a[h]
    i = l-1
    for j in range(l, h):
        if (a[j]<=pivot):
            i+=1
            (a[i], a[j]) = (a[j], a[i])
    (a[i+1], a[h]) = (a[h], a[i+1])     #Swap pivot in
    return i+1
def Quicksort(a, l, h):
    if (l<h):
        pi = partition(a,l,h)

        Quicksort(a,l,pi-1)
        Quicksort(a,pi+1,h)

n = 500000
a = np.random.randint(5000000, size = n)

start_time = time.time()
Quicksort(a, 0, n-1)
print(a)
print("--- sorting cost: %s seconds ---" % (time.time() - start_time))