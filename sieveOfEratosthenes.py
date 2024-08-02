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
