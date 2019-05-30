from __future__ import with_statement

import time


with open("matrix.txt") as f:
    lines = [line.strip().split(",") for line in f.readlines()]
    print(lines)

start = time.time()

q = {}
for i in range(159): #0 to 158 # when i is 1:
    for j in range(0, i + 1): # 0 to 1 #0,2 therefore x,y = 0, 1 take data from above, and add it. then add data from this cell as per line 20.
        x, y = j, i - j # 0, 0.
        if (0 <= x < 80) and (0 <= y < 80):
            if x == 0 and y == 0:
                q[x, y] = 0 #q[0, 0] = 0
            elif x == 0:
                q[x, y] = q[x, y - 1] #
            elif y == 0:
                q[x, y] = q[x - 1, y]
            else:
                q[x, y] = min(q[x - 1, y], q[x, y - 1])
            q[x, y] += int(lines[x][y])

print(q[79, 79])
end = time.time()
print(end-start)