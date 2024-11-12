class Solution:
    def lcmAndGcd(self, A , B):
        # Euclidean algorithm for GCD of two numbers:
#Theidea of this algorithm is, the GCD of two numbers doesn’t change if the smaller number is subtracted from the bigger number. This is the Euclidean algorithm by subtraction. It is a process of repeat subtraction, carrying the result forward each time until the result is equal to any one number being subtracted
        def gcd(A,B):
            if B==0:
                return A
            return gcd(B,A%B)
        
        x=gcd(A,B)
        y=A*B
        lcm=y//x
        lst=[lcm,x]
        return lst
        

#--------------------
#ways to do
#Prime Factorization
#Divisions by Prime
Consider a = 98 and b = 56

a = 98, b = 56:

a > b so put a = a-b and b remains same. So  a = 98-56 = 42  & b= 56. 
a = 42, b = 56:

Since b > a, we check if b%a=0. Since answer is no, we proceed further. 
Now b>a. So b = b-a and a remains same. So b = 56-42 = 14 & a= 42. 
a = 42, b = 14:

Since a>b, we check if a%b=0. Now the answer is yes. 
So we print smaller among a and b as H.C.F . i.e. 42 is  3 times of 14.
So HCF is 14. 
#Euclidean Algorithm


#--------------
# Python program to find GCD of two numbers


# Recursive function to return gcd of a and b
def gcd(a, b):

    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a

    # Base case
    if (a == b):
        return a

    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)


# Driver code
if __name__ == '__main__':
    a = 98
    b = 56
    if(gcd(a, b)):
        print('GCD of', a, 'and', b, 'is', gcd(a, b))
    else:
        print('not found')

# This code is contributed by Danish Raza


# Itervative function to return gcd of a and b


def gcd(a, b):

    # Everything divides 0
    while(a > 0 and b > 0):
        if (a > b):
            a = a % b
        else:
            b = b % a

    if (a == 0):
        return b
    return a


# Driver code
if __name__ == '__main__':
    a = 98
    b = 56
    if(gcd(a, b)):
        print('GCD of', a, 'and', b, 'is', gcd(a, b))
    else:
        print('not found')
