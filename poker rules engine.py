my_file = open("poker.txt")
lines = my_file.readlines()

dict = {'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,}

suits = {'S': 1,
         'C': 2,
         'D': 3,
         'H': 4,}

ranking = {0: 'Straight Flush',
           1: 'Quads',
           2: 'Full House',
           3: 'Flush',
           4: 'Straight',
           5: 'Trips',
           6: 'Two Pair',
           7: 'One Pair',
           8: 'High Card'}


p1_points = 0
p2_points = 0

for line in lines:
    p1_values_list = []
    p1_suits_list = []
    p2_values_list = []
    p2_suits_list = []
    p1_ranking = -1
    p2_ranking = -1
    p1_decider = -1
    p2_decider = -1


    p1 = line[0:14]
    p2 = line[15:]
    p1_cards = [p1[0:2], p1[3:5], p1[6:8], p1[9:11], p1[12:14]]
    p2_cards = [p2[0:2], p2[3:5], p2[6:8], p2[9:11], p2[12:14]]
    print(p1_cards,p2_cards)

    temp_list = []
    temp_list_2 = []

    for card in p1_cards:
        p1_values_list.append(dict[card[0]])
        p1_suits_list.append(suits[card[1]])
    p1_values_list.sort()
    p1_suits_list.sort()
    print(p1_values_list)
    print(p1_suits_list)
    #print(p1_values_list.count(p1_values_list[0]), p1_values_list.count(p1_values_list[1]), p1_values_list.count(p1_values_list[2]))
    #print(p1_values_list)

    if p1_suits_list[0] == p1_suits_list[1] == p1_suits_list[2] == p1_suits_list[3] == p1_suits_list[4] and (p1_values_list[0] == p1_values_list[1]-1 == p1_values_list[2]-2 == p1_values_list[3]-3 == p1_values_list[4]-4 or p1_values_list[0] == p1_values_list[1]-1 == p1_values_list[2]-2 == p1_values_list[3]-3 == p1_values_list[4]-12):
        p1_ranking = 0
        p1_decider = max(p1_values_list)
    elif p1_values_list.count(p1_values_list[0]) == 4 or p1_values_list.count(p1_values_list[1]) == 4:
        p1_ranking = 1
        if p1_values_list.count(p1_values_list[0]) == 4:
            p1_decider = p1_values_list[0]
        else:
            p1_decider = p1_values_list[1]
    elif (p1_values_list.count(p1_values_list[0]) == 3 and p1_values_list.count(p1_values_list[3]) ==2) or (p1_values_list.count(p1_values_list[0]) == 2 and p1_values_list.count(p1_values_list[3]) ==3):
        p1_ranking = 2
        if p1_values_list.count(p1_values_list[0]) == 3:
            p1_decider = p1_values_list[0]
        elif p1_values_list.count(p1_values_list[1]) == 3:
            p1_decider = p1_values_list[1]
        else:
            p1_decider = p1_values_list[2]
    elif p1_suits_list.count(p1_suits_list[0]) == 5:
        p1_ranking = 3
        p1_decider = max(p1_values_list)
    elif (p1_values_list[0] == p1_values_list[1] -1 == p1_values_list[2] -2 == p1_values_list[3] -3 == p1_values_list[4] -4) or (p1_values_list[0] == p1_values_list[1] -1 == p1_values_list[2] -2 == p1_values_list[3] -3 == p1_values_list[4] -12):
        p1_ranking = 4
        p1_decider = max(p1_values_list)
        if max(p1_values_list) == 14:
            p1_decider = 5
    elif (p1_values_list.count(p1_values_list[0]) == 3) or (p1_values_list.count(p1_values_list[1]) == 3) or (p1_values_list.count(p1_values_list[2]) == 3):
        p1_ranking = 5
        if p1_values_list.count(p1_values_list[0]) == 3:
            p1_decider = p1_values_list[0]
        elif p1_values_list.count(p1_values_list[1]) == 3:
            p1_decider = p1_values_list[1]
        else:
            p1_decider = p1_values_list[2]
    elif (p1_values_list.count(p1_values_list[0]) == 2 and p1_values_list.count(p1_values_list[2]) ==2) or (p1_values_list.count(p1_values_list[1]) == 2 and p1_values_list.count(p1_values_list[3]) ==2) or (p1_values_list.count(p1_values_list[0]) == 2 and p1_values_list.count(p1_values_list[3]) ==2):
        p1_ranking = 6
        for i in range(0,5):
            if p1_values_list.count(p1_values_list[i]) == 1:
                temp_list.append(p1_values_list[i])
        p1_decider = max(temp_list)
        p1_decider_2 = min(temp_list)
        for i in range(0,5):
            if p1_values_list.count(p1_values_list[i]) == 1:
                p1_decider_3 = p1_values_list[i]
    elif (p1_values_list.count(p1_values_list[0]) ==2) or (p1_values_list.count(p1_values_list[0]) ==2) or (p1_values_list.count(p1_values_list[2]) ==2) or (p1_values_list.count(p1_values_list[3]) ==2):
        p1_ranking = 7
        for i in range(0,5):
            if p1_values_list.count(p1_values_list[i]) == 2:
                temp_list.append(p1_values_list[i])
        p1_decider = max(temp_list)
        for i in range(0,5):
            if p1_values_list.count(p1_values_list[i]) == 1:
                temp_list_2.append(p1_values_list[i])
        p1_decider_2 = temp_list_2[2]
        p1_decider_3 = temp_list_2[1]
        p1_decider_4 = temp_list_2[0]
    else:
        p1_ranking = 8
        p1_decider = p1_values_list[4]
        p1_decider_2 = p1_values_list[3]
        p1_decider_3 = p1_values_list[2]
        p1_decider_4 = p1_values_list[1]
        p1_decider_5 = p1_values_list[0]



        
    for card in p2_cards:
        p2_values_list.append(dict[card[0]])
        p2_suits_list.append(suits[card[1]])
    p2_values_list.sort()
    p2_suits_list.sort()
    print(p2_values_list)
    print(p2_suits_list)
    #print(p2_values_list.count(p2_values_list[0]), p2_values_list.count(p2_values_list[1]), p2_values_list.count(p2_values_list[2]))
    #print(p2_values_list)

    temp_list = []
    temp_list_2 = []

    if p2_suits_list[0] == p2_suits_list[1] == p2_suits_list[2] == p2_suits_list[3] == p2_suits_list[4] and (p2_values_list[0] == p2_values_list[1]-1 == p2_values_list[2]-2 == p2_values_list[3]-3 == p2_values_list[4]-4 or p2_values_list[0] == p2_values_list[1]-1 == p2_values_list[2]-2 == p2_values_list[3]-3 == p2_values_list[4]-12):
        p2_ranking = 0
        p2_decider = max(p2_values_list)
    elif p2_values_list.count(p2_values_list[0]) == 4 or p2_values_list.count(p2_values_list[1]) == 4:
        p2_ranking = 1
        if p2_values_list.count(p2_values_list[0]) == 4:
            p2_decider = p2_values_list[0]
        else:
            p2_decider = p2_values_list[1]
    elif (p2_values_list.count(p2_values_list[0]) == 3 and p2_values_list.count(p2_values_list[3]) ==2) or (p2_values_list.count(p2_values_list[0]) == 2 and p2_values_list.count(p2_values_list[3]) ==3):
        p2_ranking = 2
        if p2_values_list.count(p2_values_list[0]) == 3:
            p2_decider = p2_values_list[0]
        elif p2_values_list.count(p2_values_list[1]) == 3:
            p2_decider = p2_values_list[1]
        else:
            p2_decider = p2_values_list[2]
    elif p2_suits_list.count(p2_suits_list[0]) == 5:
        p2_ranking = 3
        p2_decider = max(p2_values_list)
    elif (p2_values_list[0] == p2_values_list[1] -1 == p2_values_list[2] -2 == p2_values_list[3] -3 == p2_values_list[4] -4) or (p2_values_list[0] == p2_values_list[1] -1 == p2_values_list[2] -2 == p2_values_list[3] -3 == p2_values_list[4] -12):
        p2_ranking = 4
        p2_decider = max(p2_values_list)
        if max(p2_values_list) == 14:
            p2_decider = 5
    elif (p2_values_list.count(p2_values_list[0]) == 3) or (p2_values_list.count(p2_values_list[1]) == 3) or (p2_values_list.count(p2_values_list[2]) == 3):
        p2_ranking = 5
        if p2_values_list.count(p2_values_list[0]) == 3:
            p2_decider = p2_values_list[0]
        elif p2_values_list.count(p2_values_list[1]) == 3:
            p2_decider = p2_values_list[1]
        else:
            p2_decider = p2_values_list[2]
    elif (p2_values_list.count(p2_values_list[0]) == 2 and p2_values_list.count(p2_values_list[2]) ==2) or (p2_values_list.count(p2_values_list[1]) == 2 and p2_values_list.count(p2_values_list[3]) ==2) or (p2_values_list.count(p2_values_list[0]) == 2 and p2_values_list.count(p2_values_list[3]) ==2):
        p2_ranking = 6
        for i in range(0,5):
            if p2_values_list.count(p2_values_list[i]) == 1:
                temp_list.append(p2_values_list[i])
        p2_decider = max(temp_list)
        p2_decider_2 = min(temp_list)
        for i in range(0,5):
            if p2_values_list.count(p2_values_list[i]) == 1:
                p2_decider_3 = p2_values_list[i]
    elif (p2_values_list.count(p2_values_list[0]) ==2) or (p2_values_list.count(p2_values_list[0]) ==2) or (p2_values_list.count(p2_values_list[2]) ==2) or (p2_values_list.count(p2_values_list[3]) ==2):
        p2_ranking = 7
        for i in range(0,5):
            if p2_values_list.count(p2_values_list[i]) == 2:
                temp_list.append(p2_values_list[i])
        p2_decider = max(temp_list)
        for i in range(0,5):
            if p2_values_list.count(p2_values_list[i]) == 1:
                temp_list_2.append(p2_values_list[i])
        p2_decider_2 = temp_list_2[2]
        p2_decider_3 = temp_list_2[1]
        p2_decider_4 = temp_list_2[0]
    else:
        p2_ranking = 8
        p2_decider = p2_values_list[4]
        p2_decider_2 = p2_values_list[3]
        p2_decider_3 = p2_values_list[2]
        p2_decider_4 = p2_values_list[1]
        p2_decider_5 = p2_values_list[0]

    print("p1_ranking is: " + str(p1_ranking))
    print("p1_decider is: " + str(p1_decider))
    print("p2_ranking is: " + str(p2_ranking))
    print("p2_decider is: " + str(p2_decider))

    if p1_ranking<p2_ranking:
        p1_points += 1
    elif p2_ranking<p1_ranking:
        p2_points += 1
    elif p1_ranking==p2_ranking:
        if p1_decider>p2_decider:
            p1_points += 1
        elif p2_decider>p1_decider:
            p2_points += 1
        elif p1_decider == p2_decider:
            if p1_decider_2 > p2_decider_2:
                p1_points += 1
            elif p2_decider_2 > p1_decider_2:
                p2_points += 1
            elif p1_decider_2 == p2_decider_2:
                if p1_decider_3 > p2_decider_3:
                    p1_points += 1
                elif p2_decider_3 > p1_decider_3:
                    p2_points += 1
                elif p2_decider_3 == p1_decider_3:
                    if p1_decider_4 > p2_decider_4:
                        p1_points += 1
                    elif p2_decider_4 > p1_decider_4:
                        p2_points += 1
                    elif p2_decider_4 == p1_decider_4:
                        if p1_decider_5 > p2_decider_5:
                            p1_points += 1
                        elif p1_decider_5 < p2_decider_5:
                            p2_points +=1

    print(p1_points, p2_points)

