import time, math


def main():
    max = 1000000
    list_of_circular = []

    list = [True]*max
    start = time.time()

    list[0] = list[1] = False

    for x in range(2,math.ceil(math.sqrt(max))):
        if list[x] == True:
            for y in range(x**2, max, x):
                list[y] = False



    list_of_primes = []
    for z in range(max):
        if list[z] == True:
            list_of_primes.append(z)

    print(list_of_primes)

    for num in list_of_primes:
        test = True
        #if ("2" in str(num)) or ("4" in str(num)) or ("6" in str(num)) or ("8" in str(num)) or ("0" in str(num)) or ("5" in str(num)):
         #   test = False
        for i in range(len(str(num))):
            #print((str(num)[i:])+(str(num)[:i]))
            if list[int((str(num)[i:])+(str(num)[:i]))] == False:
                test = False
                if test == False:
                    break
        if test == True:
            list_of_circular.append(num)
        print(list_of_primes.index(num)/len(list_of_primes))

    print(len(list_of_circular), list_of_circular)
    run_time = time.time()-start
    print(run_time)

if __name__ == '__main__':
    main()