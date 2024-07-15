'''
Given a positive integer - N, print the number of multiples of 3, 5 between [1, N].

Input Format

First and only line of input contains a positive integer - N.

Constraints

1 <= N <=1018

Output Format

Print the number of multiples of 3, 5 in range of 1 to N.

Inputcopy	Outputcopy
12
6
Explanation 0

Multiples of 3 and 5 in range of 1 to 12 are 3, 5, 6, 9, 10, 12.'''

n = int(input())
c = (n // 3) + (n // 5) - (n // 15)
print(c)
