'''to access Credit card, one needs to have a income of >77000 or income which is divisible by 5.Given that the present income is 𝑋, determine if one can access credit card programs or not.If it is possible to access credit card programs, output YES, otherwise output NO.

Input Format:
The first and only line of input contains a single integer 𝑋, the persons income.

Output Format:
Print YES if it is possible to access credit card program. Otherwise, print NO.

Constraints:
0 ≤ X ≤ 108

Public Test Cases:
Test Case 1:
Input:
823

Output:
NO

'''
ars = int(input())
if ars>77000 or ars%5 == 0:print("YES")
else:print("NO")

#-------‐-----------------------------

'''Given a positive integer N, print the sum of 1st N natural numbers.

Input Format:
First and only line of input contains a positive integer - N.

Output Format:
Print the sum of 1st N natural numbers.

Constraints:
1 <= N <= 1018

Public Test Cases:
Test Case 1:
Input:
4

Output:
10

Explanation:
Test Case 2:
Input:
1

Output:
1

Explanation:
Test Case 3:
Input:
5

Output:
15
'''
ars=int(input())
summ= ars*(ars+1)// 2
print(summ)


#‐----------------------------


'''There are n switches in a house. The number of units of electricity consumed per hour when a switch is on is given. An integer k is given and the switches' indexes divisible by k are the switches that are on. Each unit costs 12 rupees. Find the bill amount of the house for 10 hours.

Input Format:
n - number of switches in the house

arr - number of units of electricity consumed when the switch is on

k - an integer that specifies which switch is on

Output Format:
The total bill amount is for 10 hours in the house.

Constraints:
1<=n<=105

1<=arr[i]<=1000

1<=k<=n

Public Test Cases:
Test Case 1:
Input:
5

1 2 3 4 5

2

Output:
720

Explanation:
Indexes divisible by 2 are 2 and 4 one-based indexes. So 2+4=6 units per hour. Then for 10 hours is 60.Then amount =12*60 = 720 rupees'''
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
t=0
for i in range(1, n + 1):
    if i % k == 0:
        t+= arr[i - 1]
total_units= t*10
total_bill =total_units * 12
print(total_bill)

#----------------------------------
