from pe46 import is_prime

def create_sieve(max):
    list = [True]*max
    list[0] = list[1] = False
    for i in range(2,max):
        if list[i] == True:
            for j in range(i+i,max,i):
                list[j] = False
    return list

def main():
    sieve = create_sieve(1000000)
    count = 0
    for x in range(len(sieve)):
        if sieve[x] == True:
            count+=1
            if count == 10001:
                print(x,count)

if __name__ == '__main__':
    main()