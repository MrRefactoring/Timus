number = int(input())
array = []
[array.append(input().split("+")) for i in range(number)]
count = 2
for i in array:
    count += len(i)
if count != 13:
    print(count*100)
else:
    print(count*100+100)
