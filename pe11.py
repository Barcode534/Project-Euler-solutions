with open("pe11.txt") as f:
    lines = f.readlines()
    print(lines)
    new = []
    for line in lines:
        line = line.rstrip("\n")
        print(line)
        new.append(line)

final = []
for line in new:
    final.append(line.split(" "))
print(final)
#print(final[0][2]) # left co ord is row. right co ord is column within row

best = 0
for y in range(0, 20): ##this does horizontal 4 in a row
    for x in range(0,20-3):
        if int(final[y][x]) *int(final[y][x+1]) * int(final[y][x+2]) * int(final[y][x+3]) > best:
            best = int(final[y][x]) *int(final[y][x+1]) * int(final[y][x+2]) * int(final[y][x+3])
            bestx = x
            besty = y

for x in range(0,20): # this does verticall ines four in a row
    for y in range(0, 20-3):
        if int(final[y][x]) *int(final[y+1][x]) * int(final[y+2][x]) * int(final[y+3][x]) > best:
            best = int(final[y][x]) *int(final[y+1][x]) * int(final[y+2][x]) * int(final[y+3][x])
            bestx = x
            besty = y

for y in range(0, 20-3):
    for x in range(0, 20-3):
        if int(final[y][x]) *int(final[y+1][x+1]) * int(final[y+2][x+2]) * int(final[y+3][x+3]) > best:
            best = int(final[y][x]) *int(final[y+1][x+1]) * int(final[y+2][x+2]) * int(final[y+3][x+3])
            bestx = x
            besty = y

for y in range(0, 20-3):
    for x in range(3, 20):
        if int(final[y][x]) *int(final[y+1][x-1]) * int(final[y+2][x-2]) * int(final[y+3][x-3]) > best:
            best = int(final[y][x]) *int(final[y+1][x-1]) * int(final[y+2][x-2]) * int(final[y+3][x-3])
            bestx = x
            besty = y

print(best, besty, bestx)