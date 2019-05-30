import math

def create_primes(max):
    list = [True] * max
    list[0] = list[1] = False

    for x in range(2, math.ceil(math.sqrt(max))):
        if list[x] == True:
            for y in range(x ** 2, max, x):
                list[y] = False

    list_of_primes = []
    for z in range(max):
        if list[z] == True:
            list_of_primes.append(z)
    return list_of_primes, list

def find_trunc(primes, is_prime):
    trun_primes = []
    for prime in primes:
        test = True
        for i in range(len(str(prime))):
            print(str(prime)[:i+1])
            print(str(prime)[i:])
            if is_prime[int(str(prime)[:i+1])] == False or is_prime[int(str(prime)[i:])] == False:
                test = False
        if test == True:
            trun_primes.append(prime)
    for remove in [2,3,5,7]:
        trun_primes.remove(remove)
    return trun_primes

def main():
    primes, is_prime = create_primes(1000000)
    print(primes)
    output = find_trunc(primes, is_prime)
    print(sum(output), output)

if __name__ == '__main__':
    main()