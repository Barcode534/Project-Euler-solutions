def check_if_amicable(n, list3):
    list1 = []
    list2 = []
    for x in range(1,n):
        if n%x==0:
            list1.append(x)

    for y in range(1,sum(list1)):
        if sum(list1)%y==0:
            list2.append(y)

    if sum(list2) == n and sum(list1)!=sum(list2): #need additional statement to remove non-uniques. was an a=b type thing. must be unique.
        list3.append(n)
    return list3

list3 = []
for i in range(1,10000):
    list3 = (check_if_amicable(i, list3))
    print(list3)
print(sum(list3))