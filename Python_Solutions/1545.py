n = int(input())
array = []
[array.append(input()) for i in range(n)]
k = input()
newarray = []
for i in array:
    if i[:1] == k:
        newarray.append(i)
[print(i) for i in newarray]
