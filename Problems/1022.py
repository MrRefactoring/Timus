def bfs(start_vertex):
    visited, queue = {start_vertex}, [start_vertex]
    while queue:
        vertex = queue.pop(0)
        for u in kid_count[vertex]:
            if u not in visited:
                visited.add(u)
                queue.append(u)
    return len(visited)

kid_count = list()
count = list()
for i in range(int(input())):
    kids = list(map(int, input().split()))[:-1]
    for kid in range(len(kids)):
        kids[kid] -= 1
    kid_count.append(kids)
for i in range(len(kid_count)):
    count.append(bfs(i))
output = str()
while True:
    maximum = max(count)
    if maximum == -1:
        break
    output += str(count.index(maximum) + 1) + " "
    count[count.index(maximum)] = -1
print(output)
