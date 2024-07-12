'''In a lively car showroom, an array of cars awaits, each with its distinctive features. Picture yourself mixing and matching these cars in unique combinations to create dream blends which has a fscore equal to the XOR value of the combination. 

You have to compute the blend score, which is the XOR of the fscore values for all these dreamy combinations. 

Input Format:
The first line of input consists of the integer n – representing the number of cars in the showroom.

The second line consists of n integers - representing the features of the car. 

Output Format:
Print the sum of fscore obtained.

Constraints:
1 <= n<= 10000
0 <= fi <= 10000
Public Test Cases:
Test Case 1:
Input:
5

﻿4 3 5 1 2

Output:
3

Explanation:
4 ^ (4^3) ^ (4^3^5) ^ (4^3^5^1) ^ (4^3^5^1^2) ^ (3) ^ (3^5) ^ (3^5^1) ^ (3^5^1^2) ^ (5) ^ (5^1) ^ (5^1^2) ^ (1) ^ (1^2) ^ 2 = 3

Test Case 2:
Input:
4

﻿1 4 5 2

Output:
0'''
ars=int(input())
lst=list(map(int,input().strip().split()))
res=0
for i in range(ars):
    summ=0
    for j in range(i,ars):
        summ^=lst[j]
        res^=summ
print(res)

#-----------------------------------------------------------------
