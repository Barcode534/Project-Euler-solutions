power = 5

super_list = []

for x in range(2,1000000):
    string = str(x)
    list = []
    for dig in string:
        #print(dig)
        list.append(int(dig))
    #print(list)
    for y in range(len(list)):
        list[y] = list[y] **power
    #print(list)
    #print(sum(list),x)
    if sum(list) == x:
        super_list.append(x)

print(super_list, sum(super_list))