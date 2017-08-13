def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            for teammate in list(team.get(vertex)):
                if type(dream_team[teammate]) == str:
                    dream_team[teammate] = dream_team[vertex] + 1
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

n = int(input())
team = dict()
for i in range(n):
    value = input().strip().split()
    for j in range(len(value)):
        addlist = team.get(value[j], set())
        if not addlist:
            team[value[j]] = addlist
        addlist.add(value[(j+1) % 3])
        addlist.add(value[(j+2) % 3])
dream_team = dict()
for i in team.keys():
    dream_team[i] = "undefined"
if "Isenbaev" not in team.keys():
    for teammate in sorted(team):
        print(teammate, "undefined")
    exit(0)
dream_team["Isenbaev"] = 0
bfs(team, "Isenbaev")
for k, v in sorted(dream_team.items()):
    print(k, v)
