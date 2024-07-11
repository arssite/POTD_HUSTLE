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
totalunits= t*10
totalbill =totalunits * 12
print(totalbill)

#----------------------------------


'''In the vast desert of the Lost Sands, there lies a hidden treasure buried beneath the dunes. Legend has it that the treasure can only be uncovered by finding the maximum sum of a subarray whose total value is less than or equal to a specific threshold value, X.



Guided by ancient maps and cryptic clues, adventurers journey into the desert, armed with their knowledge and determination. Each step brings them closer to the elusive treasure, hidden amidst the shifting sands and scorching sun.



Your task is to assist these brave souls in their quest by writing a program that calculates the sum of the most valuable subarray that meets the given condition: its sum must not exceed the threshold value X. With your help, they can uncover the riches hidden beneath the desert sands and fulfill their destiny as legendary treasure hunters.

Input Format:
The first line contains two integers separated by a space: N (the size of the array) and X (the target sum).

The second line contains N integers separated by a space, representing the elements of the array.

Output Format:
Print the sum of the subarray having the maximum sum less than or equal to the given value of X.

Constraints:
1 ≤ N ≤ 1000

1 ≤ arr[i] ≤ 104

Public Test Cases:
Test Case 1:
Input:
5 11

1 2 3 4 5

Output:
10

Explanation:
Subarray having maximum 

sum is {1, 2, 3, 4}.

Test Case 2:
Input:
5 7

2 4 6 8 10

Output:
6

Explanation:
Subarray having maximum 

sum is {2, 4} or {6}.'''
inp= input().split()
N = int(inp[0])
X = int(inp[1])
arr = list(map(int, input().split()))
sum,current,start= 0
for end in range(N):
    current+= arr[end]
    while current > X and start <= end:
        current -= arr[start]
        start += 1
    if current<= X:
        sum = max(sum, current)
print(sum)

#-------------------
