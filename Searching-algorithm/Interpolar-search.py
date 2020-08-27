import numpy as np 
def interpolationSearch(a, l, h, x): 
      
    if (l <= h and x >= a[l] and x <= a[h]): 
         pos = l + ((h - l) // (a[h] - a[l]) * (x - a[l]))                                 
   
        if a[pos] == x: 
            return pos 
  
        if a[pos] < x: 
            return interpolationSearch(a, pos + 1, h, x)
                                        
        if a[pos] > x: 
            return interpolationSearch(a, l, pos - 1, x) 
    return -1

a =  np.random.randint(30, size = 20)
n = len(a)  
a.sort()
print (a)

x = np.random.randint(30)
index = interpolationSearch(a, 0, n - 1, x)  
  
if index != -1:  
    print("Element found at index", index) 
else:  
    print("Element not found") 