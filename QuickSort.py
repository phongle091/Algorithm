import numpy as np
import time
def quickSort(a, l, r):
    n =int((l+r)/2)
    pivot = a[n]
    i = l
    j = r
    while (i < j):
        while (a[i]< pivot):
            i += 1
        while (a[j] > pivot):
            j -= 1
        if (i <= j):
            (a[i], a[j]) = (a[j], a[i])
            i += 1
            j -= 1    
        print(a)
    if (l < j):
        print("2")
        quickSort(a, l, j)    
    if (i < r):
        print("1")
        quickSort(a, i, r)
        
   
        

# n = 
# a = np.random.randint(50, size = n)
a = [6, 8, 3, 1, 5, 2, 1, 4]
n = len(a)
start_time = time.time()
quickSort(a, 0, n-1)
print(a)
print("--- sorting cost: %s seconds ---" % (time.time() - start_time))