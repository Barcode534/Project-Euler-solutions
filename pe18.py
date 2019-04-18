with open("p18.txt") as f:
    file = f.readlines()
    list = []
    for line in file:
        line = line.rstrip("\n")
        print(line)
        list.append(line)
    print(list)

new_list = []

for line in list:
    line = line.split()
    new_list.append(line)

print(new_list)
data = []
for y in range(len(new_list)):
    data.append([])

for y in range(len(new_list)):
    for x in range(len(new_list[y])):
        data[y].append(0)

data[0][0] = new_list[0][0]
print(data)

while data[len(data)-1][-1] ==0:
    for y in range(len(data)):
        for x in range(len(data[y])):
            if x==0:
                data[y][x] = int(data[y-1][x]) + int(new_list[y][x])
            elif x==len(data[y])-1:
                data[y][x] = int(data[y-1][-1]) + int(new_list[y][x])
            else:
                data[y][x] = max(int(data[y-1][x]), int(data[y-1][x-1])) + int(new_list[y][x])

    print(data)
    print(max(data[len(data)-1]))