from pe37 import create_primes
import math

def is_prime(num):
    if num ==2:
        return True
    if num %2 ==0:
        return False
    else:
        for x in range(3,int(num**0.5+1),2):
            if num%x==0:
                return False
        else:
            return True

def main():
    primes = []
    primes.append(2)
    counter = 3
    while True:
        if is_prime(counter) == True:
            primes.append(counter)
            print(primes)
        else:
            for i in primes:
                print(((counter - i) / 2) ** 0.5, int(((counter - i) / 2) ** 0.5))
                if ((counter-i)/2)**0.5 == int(((counter-i)/2)**0.5):
                    break
            else:
                print(counter)
                return counter
        counter+=2

if __name__ == '__main__':
    main()