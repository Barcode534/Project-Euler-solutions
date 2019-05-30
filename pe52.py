def main():
    num = 0
    while True:
        test = False
        num+=1
        d_count = {}
        for dig in str(num):
            if dig in d_count:
                d_count[dig] +=1
            else:
                d_count[dig] = 1
        print(num, d_count)

        for mult in range(2,7):
            test = mult*num
            test_d = {}
            for dig in str(test):
                if dig in test_d:
                    test_d[dig] +=1
                else:
                    test_d[dig] = 1
            if test_d != d_count:
                #print("Fail: " + str(num) + " " + str(test))
                break
            else:
                print("Match: " + str(num) + " " + str(test))
                test = True
        if test == True:
            break

if __name__ == '__main__':
    main()