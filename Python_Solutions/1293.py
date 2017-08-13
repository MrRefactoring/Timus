input_string = tuple(map(int, input().split()))
thorium_sulphide = 2
for i in range(len(input_string)):
    thorium_sulphide *= input_string[i]
print(thorium_sulphide)
