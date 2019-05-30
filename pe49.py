from itertools import permutations
from pe46 import is_prime
import time


def find_perm(num):
    num = str(num)
    list = []
    print(num)
    for char in num:
        list.append(int(char))
    return permutations(list)


def main():
    start = time.time()
    counter = 1489
    while counter<10000:
        test = False
        diffs = []
        output = list((find_perm(counter)))
        list_of_perm_nums = []
        for perm in output:
            string = ""
            for char in perm:
                string+= str(char)
            list_of_perm_nums.append(int(string))
        for num in list_of_perm_nums:
            if is_prime(num) == False:
                list_of_perm_nums.remove(num)
        for i in list_of_perm_nums:
            if int(i-counter) !=0:
                diffs.append(int(i-counter))
            if (int(i-counter)//2) in diffs and len(str(counter+int(i-counter))) ==4 and len(str(counter+int(i-counter))) ==4 and is_prime(counter) == True and is_prime(counter+int(i-counter)//2) == True and is_prime(counter+int(i-counter)) == True:
                print(counter, counter+int(i-counter)//2, counter+int(i-counter))
                end = time.time()
                print(end-start)
                test = True
        if test == True:
            break
        counter+=2

if __name__ == '__main__':
    main()