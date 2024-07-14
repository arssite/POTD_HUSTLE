class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        
        # code here
        summ=sum(arr)
        ex=(n*(n+1))//2
        return ex-summ
        
        #------------
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        i = 0
        while i < n - 1:
            correct = arr[i] - 1
            if arr[i] < n and arr[i] != arr[correct]:
                # Swap arr[i] and arr[correct]
                arr[i], arr[correct] = arr[correct], arr[i]
            else:
                i += 1

        for i in range(n-1):
            if i != arr[i] - 1:
                return i + 1

        return n
#-----------------------------------------
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        val = 0

        # XOR all numbers from 1 to n
        for i in range(1, n + 1):
            val ^= i

        # XOR all elements in the array
        for num in arr:
            val ^= num

        return val
#---------------------------------------------
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        arr.sort()
        
        # Iterate through the array to find the missing number
        for i in range(n-1):
            if arr[i] != i + 1:
                return i + 1
        
        # If no number is missing, return n (this line should be logically unreachable in the problem constraints)
        return n

class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        arr.sort()
        
        # Iterate through the array to find the missing number
        for i in range(n-1):
            if arr[i] != i + 1:
                return i + 1
        
        # If no number is missing, return n (this line should be logically unreachable in the problem constraints)
        return n


