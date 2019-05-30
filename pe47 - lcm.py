from pe46 import is_prime

def find_lcm(num):
    list = []
    if is_prime(num) == True:
        return [num]
    else:
        for x in range(2,int(num/2+1)):
            if num %x ==0 and is_prime(x):
                list.append(x)
        for y in list:
            if is_prime(y) == False:
                list.remove(y)
        total = 1
        for z in list:
            total*=z
        if total< num:
            if num//total in list:
                list.append(num//total)
        return list

def main():
    counter = 58569
    while True:
        print(counter)
        first = find_lcm(counter)
        second = find_lcm(counter+1)
        third = find_lcm(counter+2)
        fourth = find_lcm(counter+3)
        if len(set(first)) ==4 and len(set(second)) == 4 and len(set(third)) == 4 and len(set(fourth)) == 4:
            print(counter, counter+1, counter+2, counter+3)
            break
        else:
            if len(set(fourth))!=4:
                counter+=4
            elif len(set(third))!=4:
                counter+=3
            elif len(set(second))!=4:
                counter+=2
            else:
                counter+=1

if __name__ == '__main__':
    main()