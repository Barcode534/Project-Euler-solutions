s = [0,1,2,3,4,5,6,7,8,9]

list_of_output = []

def find_output(num):
    output = ""
    s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in num:
        output+=str(s[int(x)])
        s.pop(int(x))
    list_of_output.append(output)

def check_num(num):
    num = list(num)

    for x in range(len(num)):
        num[x] = int(num[x])

    num[-1] = int(num[-1])
    num[-1] +=1

    for y in range(-1,-len(num)-1, -1):
        if num[y] >= -y:
            num[y] = 0
            num[y-1] +=1



    for x in range(len(num)):
        num[x] = str(num[x])
    num = ''.join(num)
    print(num)
    return num



num = "0000000000"

while len(list_of_output)!=1000000:
    find_output(num)
    num = check_num(num)
    print(len(list_of_output), list_of_output[-1])
print(list_of_output[-1])