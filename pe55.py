def reverse_add(input):
    return int(input) + int(str(input)[::-1])

def main():
    count = 0
    limit = 10000
    for num in range(1,limit):
        iterations = 1
        output = reverse_add(num)
        if str(output) == str(output)[::-1]:
            print(num)
            count+=1
        while str(output) != str(output)[::-1] and iterations<50:
            output = reverse_add(output)
            iterations+=1
            if str(output) == str(output)[::-1]:
                print(num)
                count += 1
                break
    print(limit-count-1)

if __name__ == '__main__':
    main()