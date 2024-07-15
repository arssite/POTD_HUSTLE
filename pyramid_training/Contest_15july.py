'''NIET015072024 P3
0
DAYS
:
2
HRS
:
41
MINS
:
55
SECS
DEADLINE:JULY 15TH 2024, 11:00:00 PM
ChaturaIT Logo
Divider Logo
The Marvel Game
Check if the Array is Sorted
Counting Sort
Rope Cutting
The People's Nation and Democracy
 Description
 My Submissions
 Editorial
Rope Cutting
Medium
0

0

Description:
You are given N ropes. A cut operation is performed on ropes such that all of them are reduced by the length of the smallest rope. Display the number of ropes left after every cut operation until the length of each rope is zero.

Input Format:
First line contains N, number of ropes.

Next line contains N space separated integers representing ropes.

Output Format:
Print the number of ropes left after every cut operation until the length of each rope is zero.

Constraints:
1 ≤ N ≤ 105
Public Test Cases:
Test Case 1:
Input:
6

5 1 1 2 3 5

Output:
4 3 2

Explanation:
In the first operation, the minimum ropes are 1 So, we reduce length 1 from all of them after reducing we left with 4 ropes and we do the same for rest.

Test Case 2:
Input:
10

5 1 6 9 8 11 2 2 6 5

Output:
9 7 5 3 2 1

Explanation:
Self Explanatory'''
N = int(input())
ars = list(map(int, input().split()))
ars.sort()
num_ropes = N
results = []

i = 0
while i < N:
    results.append(num_ropes)
    current_length = ars[i]
    while i < N and ars[i] == current_length:
        i += 1
    num_ropes = N - i

print(' '.join(map(str, results)))


#___________________________________


'''
The People's Nation And Democracy
Easy
0

0

Description:
India is a country with a democratic government. It is time for people to choose new leaders through elections. There are completely 2 major parties Party A and Party B. There are n constituencies in the nation and each constituency vote difference between the two parties is given. All the constituencies in odd indexes go to Party A and even ones go to Party B. Return "A" if Party A wins otherwise return "B". If the majority of both parties is equal print "DRAW"

Input Format:
n - number of constituencies

arr- votes difference in each constituency

Output Format:
Print "A" if party A wins in other cases print "B" if party B wins and "DRAW" if equal.

Constraints:
1<=n<=105

1<=arr[i]<=104

Public Test Cases:
Test Case 1:
Input:
5

1 2 3 4 5

Output:
B

Explanation:
Party A majority = 2+4 (even indexes) = 6

Party B majority = 1+3+5 = 9

Party B > party A, so "B"

Test Case 2:
Input:
3

2 3 1

Output:
DRAW

Explanation:
Party A= Party B = 3, so "DRAW"'''
n = int(input())
ars = list(map(int, input().split()))

sum_A = 0
sum_B = 0

for i in range(n):
    if i % 2 == 0:
        sum_B += ars[i]
    else:
        sum_A += ars[i]

if sum_A > sum_B:
    print("A")
elif sum_B > sum_A:
    print("B")
else:
    print("DRAW")

#_________________________________

