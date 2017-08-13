number = int(input())

if 1 <= number <= 4:
    print("few")
elif 5 <= number <= 9:
    print("several")
elif 10 <= number <= 19:
    print("pack")
elif 20 <= number <= 49:
    print("lots")
elif 50 <= number <= 99:
    print("horde")
elif 100 <= number <= 249:
    print("throng")
elif 250 <= number <= 499:
    print("swarm")
elif 500 <= number <= 999:
    print("zounds")
else:
    print("legion")
