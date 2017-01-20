array = []
for i in range(3):
    j, g = map(int, input().split())
    array.append(j)
    array.append(g)
print(array[0] - array[4], array[1] - array[3])
