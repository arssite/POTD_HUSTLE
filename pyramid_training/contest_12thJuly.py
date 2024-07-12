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
'''An array containing the number x and n entries a1, a2,..., an exists.

You can choose some i and change element ai to ai & x in a single operation, where & stands for the bitwise and operation.

After performing various actions or perhaps none at all, you want the array to include at least two entries of the same type. To put it another way, ai = aj requires at least two different indices, i ≠ j. Ascertain whether the goal can be accomplished and, if so, the bare minimum of steps that need be taken.

Input Format:
The first line contains integers n and x, number of elements in the array and the number to and with.

The second line contains n integers ai , the elements of the array.

Output Format:
Print a single integer denoting the minimal number of operations to do, or -1, if it is impossible.

Constraints:
1 ≤ i ≤ n

2 ≤ n  ≤ 100 000

1 ≤ x ≤ 100 000

1 ≤ ai ≤ 100 000

Public Test Cases:
Test Case 1:
Input:
3 7

1 2 3

Output:
-1

Explanation:
Self Explanatory'''
import sys
input = sys.stdin.read().strip().split()
n = int(input[0])
x = int(input[1])
lst = list(map(int, input[2:2+n]))
oc = {}
for i in lst:
    if i in oc:
        oc[i] += 1
    else:
        oc[i] = 1
for c in oc.values():
    if c > 1:
        print(0)
        sys.exit()
and_count = {}
original_set = set(lst)
one_op_needed = False
for i in lst:
    and_result = i & x
    if and_result in and_count:
        and_count[and_result] += 1
    else:
        and_count[and_result] = 1
    if and_result in original_set and and_result != i:
        one_op_needed = True
if one_op_needed:
    print(1)
    sys.exit()
for c in and_count.values():
    if c > 1:
        print(2)
        sys.exit()
print(-1)
#---------------------------------------------------------------------------------------------

'''You are given an integer N and an index i. Your task is to check whether the ith bit is set or not in the binary representation of N.

Input Format:
The first and only line of input contains two integers N and i, separated by a space.

Output Format:
Print "True" if the ith bit is set in the binary representation of N, and "False" otherwise.

Constraints:
0 ≤ N ≤ 109

0 ≤ i ≤ 30

Public Test Cases:
Test Case 1:
Input:
10 1

Output:
True

Explanation:
The binary form of 10 is: 1010. So the 1st bit in 10 is set. Note that LSB bit is referred as 0th bit.'''
#print("Hello, World!")
ars=input().split()
N=int(ars[0])
i=int(ars[1])
mask=1 << i
is_set=(N & mask)!= 0
if is_set:print("True")
else:print("False")

#----------------------------------------------------------------------------------------------
'''Bunny is a girl who loves Shivanch restaurant menu. The menu consists of various dishes, each with a unique price. Bunny is interested in finding the minimum number of menu items needed to reach a total price of p.



Here's a list of the current menus and their prices:



           Menu	                                                                          Price

Eel flavored water	                                                          1
Deep-fried eel bones                                                      	  2
Clear soup made with eel livers	                                      4
Grilled eel livers served with grated radish                  	  8
Savory egg custard with eel	                                         16
Eel fried rice (S) 	                                                             32
Eel fried rice (L)	                                                             64
Grilled eel wrapped in cooked egg	                                128
Eel curry rice	                                                                256
Grilled eel over rice	                                                        512
Deluxe grilled eel over rice	                                           1024
Eel full-course	                                                               2048


Bunny wants to order the least number of menu items that sum up to exactly p. Each menu item can be ordered multiple times if needed.

Input Format:
The first line contains an integer T, the number of test cases. Then T test cases follow. Each test case contains an integer p.

Output Format:
For each test case, print the minimum number of menus whose total price is exactly p.

Constraints:
1 ≤ T ≤ 5

1 ≤ p ≤ 100000 (105)

There exists combinations of menus whose total price is exactly p.

Public Test Cases:
Test Case 1:
Input:
4

10

256

255

4096

Output:
2

1

8

2

Explanation:
In the first sample, examples of the menus whose total price is 10 are the following:

1+1+1+1+1+1+1+1+1+1 = 10 (10 menus)

1+1+1+1+1+1+1+1+2 = 10 (9 menus)

2+2+2+2+2 = 10 (5 menus)

2+4+4 = 10 (3 menus)

2+8 = 10 (2 menus)

Here the minimum number of menus is 2.



In the last sample, the optimal way is 2048+2048=4096 (2 menus). Note that there is no menu whose price is 4096.'''
#print("Hello, World!")
menu=[2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
res=[]
for _ in range(int(input())):
    ars=int(input())
    c=0   
    for p in menu:
        if ars == 0:
            break
        c+= ars//p
        ars %= p
    res.append(c)
for i in res:
    print(i)
#---------------------------------------------------------------------
'''Checking set bit

To check if a specific bit is set (equals 1) or not in a binary representation, you can use the bitwise AND operator (&). Here's how you can do it in pseudocode:



function is_bit_set(number, position):

  # Shift 1 to the left by the specified position

  mask = 1 << position



  # Use bitwise AND to check if the bit is set

  return (number & mask) != 0

In this pseudocode:



i )  1 << position creates a mask with a 1 at the specified position by left-shifting the binary digit 1 to the left by the given position.

ii )  (number & mask) != 0 checks if the bit at the specified position is set by performing a bitwise AND operation. If the result is not zero, it means the bit is set.



Task

Write a program that takes an input integer N and prints the count of the set bits present in the number.



Input Format:
The input consists of a single integer N, representing the number for which the count of set bits needs to be calculated.

Output Format:
Output a single integer, representing the count of set bits in the binary representation of the input number N

Constraints:
1 <= N <= 1000

Public Test Cases:
Test Case 1:
Input:
256

Output:
1

Explanation:
For 

N = 256, which is 1000000002 in binary representation, there is only one bit set to 1 (the 9th bit from the right) and the rest are all zeros. Therefore, the count of set bits in N is 1.

Test Case 2:
Input:
15

Output:
4

Explanation:
For 

N = 15, which is 11112 in binary representation, all four bits are set to 1. Therefore, the count of set bits in N is 4.'''
#print("Hello, World!")
ars=int(input())
c=0
while ars>0:
    if ars & 1:c+= 1
    ars >>= 1
print(c)
