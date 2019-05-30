def caps_to_num(letter):
    output = ord(letter) - 64
    return output

def evaluate_word(word):
    for char in word:
        print("hello")

def main():
    list = []
    max = 1000
    triangle = 0
    for x in range(1,max):
        list.append(int(0.5*x*(x+1)))
    print(list)
    print(caps_to_num('A'))
    with open("p42.txt") as f:
        words = f.read().split(",")
        print(words)
        for word in words:
            word = word.rstrip("\"").lstrip("\"")
            print(word)
            total = 0
            for char in word:
                print(caps_to_num(char))
                total+= caps_to_num(char)
            if total in list:
                triangle+=1
    print(triangle)


if __name__ == '__main__':
    main()