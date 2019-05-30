def fact(n):
    factorial = 1
    for x in range(n,0,-1):
        factorial *=x
    return factorial

def sum_dig(input):
    string = str(input)
    sum = 0
    for dig in string:
        sum+=int(dig)
    return sum

print(fact(100))
print(sum_dig(fact(100)))