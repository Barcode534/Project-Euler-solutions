from pe37 import create_primes
from itertools import permutations

def main():
    # print(sum(int(”.join(x)) for x in permutations(‘0123456789’, 10) if all([not int(”.join(x)[n[0]:n[1]]) % n[2]
    # for n in [(1, 4, 2), (2, 5, 3), (3, 6, 5), (4, 7, 7), (5, 8, 11), (6, 9, 13), (7, 10, 17)][:7]])))
    pan = []
    div = [2,3,5,7,11,13,17]
    for x in permutations('0123456789',10):
        string = ""
        test = True
        for num in x:
            string+=str(num)
        print(string)
        for y in range(len(div)):
            print(string[y+1:y+4], div[y])
            if int(str(string)[y+1:y+4]) % div[y] !=0:
                test = False
                break
        if test == True:
            pan.append(int(string))
    print(pan, sum(pan))

if __name__ == '__main__':
    main()