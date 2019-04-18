small_primes = [2,3,5,7,11,13,17,19]
list_of_lists = []
dict = {}

for x in range(1,21):
    list_of_lists.append([])
    for y in small_primes:
        if x%y==0:
            list_of_lists[x-1].append(y)
            #list_of_lists[x-1]*=int((x/y))
        if (x/y)%y==0:
            list_of_lists[x-1].append(y)
        if (x/y)/y%y==0:
            list_of_lists[x-1].append(y)
        if (x/y)/y/y%y==0:
            list_of_lists[x-1].append(y)


print(list_of_lists)

for x in range(1,21):
    dict[x] = 0
    for list in list_of_lists:
        if list.count(x) > dict[x]:
            dict[x] = list.count(x)

print(dict)
lcm = 1
for key in dict:
    for _ in range(dict[key]):
        lcm*=key

print(lcm)