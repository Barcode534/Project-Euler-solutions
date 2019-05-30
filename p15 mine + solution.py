import time

list = []

for y in range(0,21):
    list.append([])
    for x in range(0,21):
        list[y].append(0)



for x in range(0,21):
    y=20
    list[y][x] = 1

for y in range(0,21):
    x=20
    list[y][x] =1

for line in list:
    print(line)

while list[0][0]==0:
    for y in range(0,20):
        for x in range(0,20):
            if list[y][x] ==0 and list[y+1][x] != 0 and list[y][x+1]!=0:
                list[y][x] = list[y+1][x] + list[y][x+1]
    for line in list:
        print(line)


def route_num(cube_size):
    L = [1] * cube_size
    print("\n\n")
    print(L)
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j] + L[j - 1]
        L[i] = 2 * L[i - 1]
        print(L)
    return L[cube_size - 1]


start = time.time()
n = route_num(20)
elapsed = (time.time() - start)
print("%s found in %s seconds" % (n, elapsed))