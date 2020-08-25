import numpy as np
import time

def merge(a, l, m, r):
    #create Left and Right array\
    (L, R) = ([], [])
    for i in range(m-l+1):
        L.append(a[l + i])
    for j in range(r-m):
        R.append(a[m + j + 1])

    # Merging
    (i, j, k) = (0, 0, l)
    while(i < m-l+1 and j < r-m):
        if(L[i] <= R[j]):
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j +=1
        k +=1
    while(i < m-l+1):
        a[k] = L[i]
        i += 1
        k += 1
    while(j < r-m):
        a[k] = R[j]
        j += 1
        k += 1
    

def Merge_Sort(a, l, r):
    if (l < r):
        mid = int((l+r)/2)
        Merge_Sort(a, l, mid)
        Merge_Sort(a, mid+1, r)
        merge(a, l, mid, r)

n = 5000
a = np.random.randint(500000, size = n)


start_time = time.time()
Merge_Sort(a, 0, n-1)
print(a)
print("--- sorting cost %s seconds ---" % (time.time() - start_time))