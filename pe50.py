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
    max = 1000000
    sieve = create_sieve(max)
    print(sieve)
    best_total = 0
    best_terms = 0
    for x in range(2,max):
        total = 0
        terms =0
        for y in range(x,max):
            if sieve[y] == True:
                total+=y
                terms +=1
                if total<max and sieve[total] == True:
                    #print(y, total, terms)
                    if terms > best_terms:
                        best_terms = terms
                        best_total = total
                        print("best: " + str(best_total) + str(" ") + str(best_terms))
            if total>=max:
                break

        #print("\n")

if __name__ == '__main__':
    main()