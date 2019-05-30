def function():
    best = 0
    list = []

    for x in range(1,1000000):
        list= []
        list.append(x)
        while x!=1:
            if x%2==0:
                x = x/2
            else:
                x = (3*x)+1
            list.append(x)
        if x ==1:
            length = len(list)
            if length>best:
                best = length
                print(list)
                print(best)
                list = []
        # length = len(list)
        # if length>best:
        #     best = length
        #     print("best is: " + str(best))


function()