import sys
n = tuple(map(float, sys.stdin.read().split()[::-1]))
for i in n:
    print("{:.4f}".format(i**0.5))
