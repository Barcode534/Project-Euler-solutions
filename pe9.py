for a in range(0,999):
    for b in range(a+1,999):
        for c in range(b+1,999):
            if a+b+c ==1000 and a**2 + b**2 == c**2:
                print(a,b,c)
    print(a/999)