from pe37 import create_primes

def main():
    max = 100000000
    pan_dig = []
    primes, is_prime = create_primes(max) # list of prime numbers. and list of False/True 0,1,2,3... for prime True or False
    for num in primes:
        test = True
        for x in range(1,1+len(str(num))):
            if str(num).count(str(x)) != 1:
                test = False
                break
        if test == True:
            pan_dig.append(num)
    print(pan_dig)


if __name__ == '__main__':
    main()