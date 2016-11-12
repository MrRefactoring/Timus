array = []
[array.append(int(input())) for i in range(int(input()))]
array.sort()
[print(array[i]) for i in range(len(array) - 1, -1, -1)]
