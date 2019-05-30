def main():
    highest = 0
    for a in range(1,100):
        for b in range(1,100):
            sum = 0
            for dig in str(a**b):
                sum +=int(dig)
            if sum>highest:
                highest = sum
    print(highest)

if __name__ == '__main__':
    main()