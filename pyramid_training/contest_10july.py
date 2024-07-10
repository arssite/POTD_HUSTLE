#Length Of Last Word
ars = input().strip()
words = ars.split()
print(len(words[-1]))

#Reverseboard
ars = input()
result = []
for char in ars:
    if char == 'i':
        result.reverse()
    else:result.append(char)
print(''.join(result))


#ChaturaIT Contest
ars = int(input().strip())
for i in range(1, 10):
    same_digit_number = int(str(i) * 3)
    if same_digit_number >= ars:
        print(same_digit_number)
        break

#Facing The Sun
ars=int(input())
H=list(map(int, input().strip().split()))
max_height=0
count=0
for height in H:
    if height>max_height:
        count += 1
        max_height = height
print(count)
