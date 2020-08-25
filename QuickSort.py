import numpy as np

def quickSort(a, l, r):
    n =int((l+r)/2)
    pivot = a[l]
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
    if (i < r):
        quickSort(a, i, r)
    if (l < j):
        quickSort(a, l, j)

n = 5
a = np.random.randint(50, size = n)
quickSort(a, 0, n-1)
print(*a)