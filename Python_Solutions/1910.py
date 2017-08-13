input()
field = [int(value) for value in input().split()]
max_window = 0
start_window_index = 0
for i in range(len(field)-2):
    window = [field[i], field[i+1], field[i+2]]
    if sum(window) >= max_window:
        max_window = sum(window)
        start_window_index = i
print(max_window, start_window_index + 2)
