import math

def ncr(n,r):
    return int(math.factorial(n) / ((math.factorial(r) * math.factorial(n-r))))

def main():
    counter = 0
    for n in range(1,101):
        for r in range(n+1):
            if ncr(n,r) > 1000000:
                counter+=1
    print(counter)
    return counter

if __name__ == '__main__':
    main()