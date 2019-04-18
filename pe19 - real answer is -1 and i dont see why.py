month_length_dict = {1:31,
                     2:28,
                     2.5:29,
                        3:31,
                        4:30,
                        5:31,
                        6:30,
                        7:31,
                        8:31,
                        9:30,
                        10:31,
                        11:30,
                        12:31}

total = 0

for x in range(1,13):
    total += month_length_dict[x]
print(total)

day = 1
month = 1
year = 1901
dayofweek = 1

counter = 0
days_elapsed = 0
while year<2001:
    if dayofweek==7 and day ==1:
        counter +=1
        print(day, month, year, dayofweek, counter, days_elapsed)
    day +=1
    dayofweek+=1
    if dayofweek>7:
        dayofweek=1
    if day>month_length_dict[month]:
        day=1
        month+=1
        if month==2 and year%4==0:
            month=2.5
        if month==3.5:
            month=3
    if month>12:
        month=1
        year+=1
    if year>2000:
        break


    days_elapsed +=1

