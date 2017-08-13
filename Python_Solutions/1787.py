howMuch, minutes = map(int, input().split())
array = tuple(map(int, input().split()))
carsCount = 0
for carsNow in array:
    if carsNow <= howMuch:
        carsCount -= howMuch-carsNow
        if carsCount < 0:
            carsCount = 0
    else:
        carsCount += carsNow - howMuch
print(carsCount)
