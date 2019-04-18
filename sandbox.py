def non_abun():
    list = []
    for x in range(1,28124):
        list.append(x)

    list2 = []
    for x in range(1,28124):
        check_abun = []
        for y in range(x-1,0,-1):
            if x%y==0:
                check_abun.append(y)
                print(check_abun)
        if sum(check_abun)>x:
            list2.append(x)
            print(list2)

    return list, list2

print(non_abun())