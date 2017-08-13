def bin_search(array, number):
    lo = 0
    hi = len(array)
    while lo < hi:
        mid = (lo + hi) // 2
        midval = array[mid]
        if midval < number:
            lo = mid + 1
        elif midval > number:
            hi = mid
        else:
            return True
    return False

psychup = [[], [], []]
minimal, index = 10000, 0
for i in range(len(psychup)):
    value = int(input())
    if minimal > value:
        index = i
        minimal = value
    psychup[i] = [int(v) for v in input().split()]
global_count = 0
for i in psychup.pop(index):
    if bin_search(psychup[0], i):
        pass
    else:
        continue
    if bin_search(psychup[1], i):
        global_count += 1
print(global_count)
