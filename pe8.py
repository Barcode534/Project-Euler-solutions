string = ""

with open("pe8.txt") as f:
    text = f.readlines()
    print(text)
    for line in text:
        line = line.rstrip("\n")
        string += line

    print(string)
    print(len(string))
    best = 0
    for x in range(0,len(string)-13):
        print(string[x:x+13])
        test = string[x:x+13]
        value = 1
        for val in test:
            value *= int(val)
        if value > best:
            best = value
    print(best)