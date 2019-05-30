def main():
    dec = "0."
    ignore = len(dec)-1
    for x in range(1,1000000):
        dec+= str(x)
    #print(dec)
    list = [1,10,100,1000,10000,100000,1000000]
    solution = 1
    for item in list:
        solution *= int(dec[ignore+item])
        print(int(dec[ignore+item]))
    print(solution)

if __name__ == '__main__':
    main()