number = int(input())
lst = list()
count = 0
for i in range(number):
    value = input()
    if value in lst:
        lst.append(value)
        count += 1
    else:
        lst.append(value)
print(count)
