#if arr=[010101] then [000111]
arr.sort()
#---------------
lst1=[]
lst0=[]
for i in arr:
  if i&1==1:
    lst1.append(i)
  else:
    lst0.append(i)
arr.clear()
arr[:]=lst0+lst1
#--------------------
from collections import deque
lst=[]
lst=deque(lst)
for i in arr:
  if i==1:
    lst.append(i)
  else:
    lst.appendleft(i)
  
    
