full = []

square_size = 1003
start = int((square_size-1)/2)
print(start)

for y in range(0,square_size):
    row = []
    for x in range(0,square_size):
        row.append(0)
    full.append(row)

full[start][start] = 1
#full[start][start+1] = 2
for line in full:
    print(line)
x,y = start, start
while full[1][square_size-2] ==0 and 1<=x<=square_size-1 and 1<=y<=square_size-1:
    #print(full[y][x])
    if full[y+1][x] ==0 and full[y-1][x] ==0 and full[y][x+1]==0 and full[y][x-1]==0:
        full[y][x+1] = full[y][x] +1
        x,y = x+1, y
    if full[y][x-1] != 0 and full[y+1][x] == 0 and full[y-1][x] == 0 and full[y][x+1] == 0:
        full[y+1][x] = full[y][x] +1
        x,y = x, y+1
    if full[y-1][x] !=0 and full[y+1][x] ==0 and full[y][x+1]==0 and full[y][x-1]==0:
        full[y][x-1] = full[y][x] +1
        x,y = x-1, y
    if full[y][x+1] !=0 and full[y-1][x] !=0 and full[y][x-1]==0 and full[y+1][x]==0:
        full[y][x-1] = full[y][x] +1
        x,y = x-1, y
    if full[y][x+1] !=0 and full[y][x-1] ==0 and full[y+1][x]==0 and full[y-1][x]==0:
        full[y-1][x] = full[y][x] +1
        x,y = x, y-1
    if full[y+1][x] !=0 and full[y][x+1] !=0 and full[y-1][x]==0 and full[y][x-1]==0:
        full[y-1][x] = full[y][x] +1
        x,y = x, y-1
    if full[y+1][x] !=0 and full[y-1][x] ==0 and full[y][x+1]==0 and full[y][x-1]==0:
        full[y][x+1] = full[y][x] +1
        x,y = x+1, y
    if full[y][x-1] !=0 and full[y+1][x] !=0 and full[y][x+1]==0 and full[y-1][x]==0:
        full[y][x+1] = full[y][x] +1
        x,y = x+1, y
    if full[y][x-1] !=0 and full[y+1][x] !=0 and full[y][x+1]==0 and full[y-1][x]==0:
        full[y][x+1] = full[y][x] +1
        x,y = x+1, y
    try:
        if full[y][x+1] ==0 and full[y+1][x] ==0:
            full[y+1][x] = full[y][x] +1
            x,y = x, y+1
    except:
        for line in full:
            print(line)
        print("\n")
        break
    if full[y][x+1] ==0 and full[y-1][x] ==0:
        full[y][x+1] = full[y][x] +1
        x,y = x+1, y

print("\n")
for line in full:
    print(line)
print("\n")
sum = 0
for z in range(0,square_size):
    sum+=full[z][z]
    print(full[z][z])
q=square_size-1
for p in range(0,square_size):
    sum+= full[q][p]
    print(full[q][p])
    q-=1
sum-=full[start][start]
print(-full[start][start])
print(sum)