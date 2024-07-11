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
