#linearSearch
'''
def search(arr, N, x):
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1
    
    
x=list(map(int,input().split()))
a=int(input("Enter Searching Element: "))
print(search(x,len(x),a))
'''

#____________________________________________________________________
def binarySearch(arr, low,high,x):
    if high >= low:
        mid = low + (high - low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, high, x)

    # Element is not present in the array
    else:
        return -1
        
        
arr=list(map(int,input("enter array:  ").split()))
print(arr)
x=int(input("enter Value: "))
print(binarySearch(arr,0,len(arr)-1,x))
