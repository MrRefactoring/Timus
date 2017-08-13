num, digit = map(str, input().split())
num, digit = int(num), len(digit)
value = 1
last = 1
if num % digit != 0:
    last = num % digit
while num != num % digit:
    value *= num
    num -= digit
print(value*last)
