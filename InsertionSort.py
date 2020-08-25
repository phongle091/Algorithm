import numpy as np
n = 100
a = np.random.randint(1000, size = n)

def insertionSort(a, n):
    for i in range(n):
        index = i
        value = a[i]
        while (index > 0 and a[index - 1] > value):
            a[index] = a[index - 1]
            index -= 1
        a[index] = value
    return a

insertionSort(a, n)
print(*a)