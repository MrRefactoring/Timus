array = tuple(map(int, input().split()))
numbers = int(input())
count = 1
for i in range(numbers):
    s = input()
    if s == "Blue":
        count *= array[0]
    elif s == "Red":
        count *= array[1]
    elif s == "Yellow":
        count *= array[2]
print(count)