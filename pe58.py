def create_sieve(input):
    sieve = [True] * (input +1)
    sieve[0] = sieve[1] = False
    for num in range(2,int((input+1)/2)):
        if sieve[num] == True:
            i = num+num
            while i<=input:
                sieve[i] = False
                i+=num
    print(sieve)
    return sieve

def is_prime(input):
    if input%2 ==0 and input!=2:
        return False
    else:
        for div in range(3,int(input**0.5+1),2):
            if input%div == 0:
                return False
        else:
            return True

def main():
    size = 100000000
    max = 11
    #sieve = create_sieve(size)
    set_all = 1
    set_prime = 0
    ratio = 1
    length = 3
    while ratio>0.1:
        corner = length**2
        second = corner - (length-1)
        third = second - (length-1)
        fourth = third - (length-1)
        values = [corner, second, third, fourth]
        for value in values:
            set_all+=1
            if is_prime(value) == True:
                set_prime+=1
        ratio = set_prime/set_all
        print(ratio)
        length+=2


        print(corner, second, third, fourth)


    ##in terms of lines, we have 1,3,13,31
    ## with stats of line:       1,2,3, 4
    ## length of                 1,3,5, 7
    ## perim of                  1,8,24,48
    ## bottom right corner is always the square of the length

if __name__ == '__main__':
    main()