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
