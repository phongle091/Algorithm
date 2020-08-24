import numpy as np

a = np.random.randint(100, size = 30)
print(a)
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def BubbleSort(a):
    n = len(a)
    for j in range(n-1):
        for i in range(n-j-1):
            if a[i] > a[i+1]:
                (a[i], a[i+1]) = swap(a[i], a[i+1])
            # else: continue
    return a
a = BubbleSort(a)
print(a)
