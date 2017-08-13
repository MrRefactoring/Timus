number = int(input())
count = 0
position = 1
for i in range(number):
    mail = input()[:1]
    if mail in ("A", "R", "O", "P"):
        if position == 2:
            count += 1
            position = 1
        elif position == 3:
            count += 2
            position = 1
    elif mail in ("M", "B", "S"):
        if position == 1:
            count += 1
            position = 2
        elif position == 3:
            count += 1
            position = 2
    elif mail in ("T", "D", "J", "K", "G", "W"):
        if position == 1:
            count += 2
            position = 3
        elif position == 2:
            count += 1
            position = 3
print(count)
