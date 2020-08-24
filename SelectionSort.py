import numpy as np

a = np.random.randint(100,size=30)
n = len(a)
def SelectionSort(a, n):
    
    for i in range(n-1):
        value = a[i]
        index = i
        for j in range (i+1, n):
            if (a[index] > a[j]):
                index = j

        if (i != index):
            temp = a[i]
            a[i] = a[index]
            a[index] = temp
    return a
a = SelectionSort(a,n)
print(*a)