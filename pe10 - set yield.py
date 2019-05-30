def erath(n):
    mult = set() # init set
    for i in range(2,n+1): # 2 to 2m range
        if i not in mult: # if a number doesnt exist in the set, add it in the list, by itself. No higher multiples of it needed, as the initial number will include all higher multiples.
            yield i # this adds to the list? the prime number?
            mult.update(range(i*i, n+1, i)) # this adds all numbers to mult, to include all numbers 2 to 2m
            if i ==5:
                print(mult)

iter = 0
ml = list(erath(2000000))
print(ml)
for x in ml:
    iter = int(x) + iter # this adds all of the yielded i's, I think? All the prime nums at their first (and only) occurance

print(iter)