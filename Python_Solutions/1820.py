import sys

for i in sys.stdin:
    a, b = map(int, i.split())
    t = a / float(b)
    if 0 < t <= 0.5:
        print(2)
    elif 0.5 < t <= 1.0:
        print(2)
    elif 0 < (t - int(t)) <= 0.5:
        print(int(t) * 2 + 1)
    elif 0.5 < (t - int(t)) < 1.0:
        print(int(t) * 2 + 2)
    else:
        print(int(t) * 2)
