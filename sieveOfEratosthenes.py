class Solution:
    def sieveOfEratosthenes(self, N):
    	#code here 
    	def prim(n):
    	    if n<2:
    	        return False
    	    for i in range(2,int(n**0.5)+1):
    	        if n%i==0:
    	            return False
    	    return True
    	out=[]
    	for i in range(N+1):
    	    if prim(i):
    	        out.append(i)
    	return out

# https://www.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [1] * n
        for i in range(2, int(n**0.5) + 1):
            if prime[i] == 1:
                for j in range(i*i, n, i):
                    prime[j] = 0
        
        ans = 0
        for i in range(2, n):
            if prime[i] == 1:
                ans += 1
        
        return ans
