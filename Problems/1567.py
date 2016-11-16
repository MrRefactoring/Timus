string = input()
price = 0
for i in range(len(string)):
    if string[i] in ("a", "d", "g", "j", "m", "p", " ", "s", "v", "y", "."):
        price += 1
    elif string[i] in ("b", "e", "h", "k", "n", "q", "t", "w", "z", ","):
        price += 2
    else:
        price += 3
print(price)
