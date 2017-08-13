Ticket = int(input())
b = str(Ticket + 1)
q = str(Ticket - 1)
while len(b) < 6:
    b = str(0) + b
while len(q) < 6:
    q = str(0) + q
p1, p2 = int(int(b[0])+int(b[1])+int(b[2])), int(int(b[3])+int(b[4])+int(b[5]))
g1, g2 = int(int(q[0])+int(q[1])+int(q[2])), int(int(q[3])+int(q[4])+int(q[5]))
if p1 != p2 and g1 != g2:
    print("No")
else:
    print("Yes")
