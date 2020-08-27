n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
x = int(input())
temp = -1
for i in range(n):
    if (x == a[i]):
        print(i)
        temp = i
        break
if (temp == -1):
    print(temp)
    