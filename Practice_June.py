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

Q:https://www.codechef.com/practice/course/arrays-strings-sorting/INTARR01/problems/DOMINANT2
for _ in range(int(input())):
    n=int(input())
    lst=map(int,input().split())
    items=[0]*(n+1)
    # print(items)
    for i in lst:
        items[i]+=1
        # print(items)
    max_i=max(items)
    print('yes' if items.count(max_i)==1 else 'no')
