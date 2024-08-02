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
    def prime_Sum(self, n):
        if n < 2:
            return 0

        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False

        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1

        prime_sum = sum(i for i in range(n + 1) if is_prime[i])
        return prime_sum

# Example usage:
sol = Solution()
print(sol.prime_Sum(50))  # Example to get the sum of all primes up to 50
#-------------------------------------

#O(n)
class Solution:
    def sieveOfEratosthenes(self, N):
    	#code here 
    	prime=[]
    	is_prime=[True]*(N+1)
    	for i in range(2,N+1):
    	    if is_prime[i]:
    	        prime.append(i)
    	    for j in prime:
    	        if i*j>N:
    	            break
    	        is_prime[i*j]=False
    	        if i%j==0:
    	            break
    	return prime


#---------------------------Segmented Sieve product-------------------------------------------

from math import sqrt

class Solution:

    # Function to check if a number is prime.
    def prime(self,n):
        if n==1 or n==0:
            return False
        if n==2 or n==3:
            return True
        if n%2==0 or n%3==0:
            return False
        for i in range(5,int(sqrt(n))+1,6):
            if n%i==0 or n%(i+2)==0:
                return False
        return True

    # Function to calculate the product of prime numbers within the given range.
    def primeProduct(self, L, R):
        d=1
        for i in range(L,R+1):
            if self.prime(i):
                d=d*i
                d=d%(10**9+7)
        return d%(10**9+7)
