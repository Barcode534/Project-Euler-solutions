def main():
    ts = set()
    ps = set()
    hs = set()

    i=284
    while True:
        i+=1
        ts.add((i**2 + i) //2)
        ps.add((((3*i**2)-i))//2)
        hs.add((2*i**2)-i)
        if (i**2 + i) //2 in ts and (i**2 + i) //2 in ps and (i**2 + i) //2 in hs:
            print((i**2 + i) //2)
            #print(ts,ps,hs)
            return (i**2 + i)


if __name__ == '__main__':
    main()