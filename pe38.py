def main():
    pan = []
    for x in range(1, 10000):
        print(x)
        for i in range(3,20):
            ns = []
            str_collect = []
            for n in range(1, i):
                ns.append(n)
            for num in ns:
                str_collect.append(str(x * num))
                value = ""
            for chars in str_collect:
                value += chars
            print(value)
            if len(str(value)) == 9 and str(value).count("1") == 1 and str(value).count("2") == 1 and str(value).count(
                "3") == 1 and str(value).count("4") == 1 and str(value).count("5") == 1 and str(value).count(
                "6") == 1 and str(value).count("7") == 1 and str(value).count("8") == 1 and str(value).count("9") == 1:
                pan.append(value)
    print(pan)

if __name__ == '__main__':
    main()