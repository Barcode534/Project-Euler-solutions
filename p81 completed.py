import time

with open ("matrix.txt") as f:
    lines = [line.strip().split(",") for line in f.readlines()]
    print(lines)

start = time.time()

q = {} #start empty dict to store data


for i in range(0,80):
    for j in range(0,80):
        q[i, j] = 0

q[0, 0] = lines[0][0]

for x in range(1,80):
    q[0, x] += int(q[0, x-1]) + int(lines[0][x])

for y in range(1,80):
    q[y, 0] += int(q[y-1, 0]) + int(lines[y][0])

for x in range(1,80):
    for y in range(1, 80):
        q[y, x] += min((q[y-1, x]), q[y, x-1]) + int(lines[y][x])

print(q[79, 79])

end = time.time()
print(end-start)