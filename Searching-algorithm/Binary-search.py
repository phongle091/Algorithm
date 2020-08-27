n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
x = int(input())
def binsearch(a, x, n):
    l = 0
    r = n-1
    while (l < r):
        mid = int((l+r)/2)
        if (a[mid] < x):
            l = mid + 1     #tranh truong hop r = x, lap vo han.
        else:
            r = mid 

    if (a[l] == x):
        print(l)
      
    else:
        print(-1)

binsearch(a, x, n)