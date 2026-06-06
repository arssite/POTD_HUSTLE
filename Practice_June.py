# Q : https://www.codechef.com/practice/course/arrays-strings-sorting/INTARR01/problems/EQUALELE
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    dic={}
    for i in lst:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    print(n-max(dic.values()))

