st=input()
vowels = set('aeiouAEIOU')
for i in st:
  if i not in vowels:
    print("No")
    break
else:
  print("Yes")
