doubles = [2]


def the_next():
    result = 1
    for i in doubles:
        result *= i
    return result + 1


count = int(input())

for i in range(1, count):
    doubles.append(the_next())

for i in doubles:
    print(i)

