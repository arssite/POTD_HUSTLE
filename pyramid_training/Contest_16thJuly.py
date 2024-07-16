'''NIET016072024 P3
0
DAYS
:
2
HRS
:
36
MINS
:
39
SECS
DEADLINE:JULY 16TH 2024, 11:00:00 PM
ChaturaIT Logo
Divider Logo
Find the Number of Unlit Candles
World of Coders
Maximum Number of Funded Temples
Tertiary Maximum Finder
 Description
 My Submissions
 Editorial
Tertiary Maximum Finder
Easy
0

0

Description:
Given an integer array A, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Input Format:
First line contains n, the size of the array.

Next line contains n space-separated integers.

Output Format:
An integer representing the third distinct maximum number in the input array. If the third maximum does not exist, the maximum number from the input array is returned.

Constraints:
1 <= A.length <= 104

-231 <= A[i] <= 231 - 1

Public Test Cases:
Test Case 1:
Input:
3

3 2 1

Output:
1

Explanation:
Self Explanatory

Test Case 2:
Input:
2

1 2

Output:
2

Explanation:
Self Explanatory'''
n = int(input())
ars = list(map(int, input().split()))
dmax = sorted(set(ars), reverse=True)
if len(dmax) >= 3:print(dmax[2])
else:print(dmax[0])


#___________________________________

'''2
1 2NIET016072024 P3
0
DAYS
:
2
HRS
:
42
MINS
:
11
SECS
DEADLINE:JULY 16TH 2024, 11:00:00 PM
ChaturaIT Logo
Divider Logo
Find the Number of Unlit Candles
World of Coders
Maximum Number of Funded Temples
Tertiary Maximum Finder
 Description
 My Submissions
 Editorial
Maximum Number Of Funded Temples
Medium
0

0

Description:
In a state, there are n temples which are funded by the government. But as of the fact, the funds will not be sufficient for all the temples. Some temples receive a lot of pilgrims and so require more amenities whereas some temples require few funds so government should not distribute the funds equally.

So government came up with the idea of funding as many temples as possible and the left over temples will be funded in the course of government continuation. An array is given representing the funds required in lakhs. An integer k is given which is the total fund released by the government. Find the maximum number of temples that the government can fund in the current course.

Input Format:
n - Number of temples

arr - Funds required by each temple in Lakhs

k - Fund released by government in lakhs

Output Format:
Maximum number of temples that can be funded based on the requirement.

Constraints:
1<=n<=105

1<=arr[i]<=1000

1<=k<=107

Public Test Cases:
Test Case 1:
Input:
5

1 2 4 6 7

10

Output:
3

Explanation:
10 lakh fund can be distributed among temples 1,2 and 4 with required funds as 1,2,6 whose sum is less than 10.'''

n = int(input())
ars = list(map(int, input().split()))
k = int(input())
ars.sort()
total= 0
temples_funded = 0
for fund in ars:
    if total + fund <= k:
        total+= fund
        temples_funded += 1
    else:
        break
print(temples_funded)


#___________________________________

'''
P3
0
DAYS
:
2
HRS
:
59
MINS
:
12
SECS
DEADLINE:JULY 16TH 2024, 11:00:00 PM
ChaturaIT Logo
Divider Logo
Find the Number of Unlit Candles
World of Coders
Maximum Number of Funded Temples
Tertiary Maximum Finder
 Description
 My Submissions
 Editorial
Find The Number Of Unlit Candles
Medium
0

0

Description:
There are n rooms. Each room contains several candles. A matchbox is given and it has x number of matchsticks in it. It is observed that one room needs 1 matchstick to light all the candles in it.

Arya Stark is given the job of lighting up the candles. Help Arya Stark to light up as many candles as possible. Return the unlit candles.

Do not use sorting. (try)

Input Format:
n- number of rooms

arr - an array of integers representing the number of candles in each room.

m- number of matchsticks in the matchbox

Output Format:
Number of unlit candles

Constraints:
1<=n<=2*106

1<= arr[i] <=106

1<=m<=106

Public Test Cases:
Test Case 1:
Input:
4

1 9 3 600

3

Output:
1

Explanation:
The lit rooms have 9,3,600 and the left room without a matchstick is the room with 1 candle. So unlit candles=1

Test Case 2:
Input:
7

1 1 1 1 3 4 7

4

Output:
3

Explanation:
3,4,7 are lit along with one room with one candle. With this, all the matchsticks are exhausted. There are 3 left room with 1 matchstick each.

So unlit candles = 3'''

n = int(input())
ars = list(map(int, input().split()))
m = int(input())
if m >= n:
    unlit_candles = 0
else:
    unlit_rooms = n - m
    ars.sort()
    unlit_candles = sum(ars[:unlit_rooms])
print(unlit_candles)



#_________________________________

