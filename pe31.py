combos = 0
goal = 200


for a in range(goal,-1,-200):
    for b in range(a, -a,-100):
        for c in range(b,-b,-50):
            for d in range(0,11):
                for e in range(0,21):
                    for f in range(0,41):
                        for g in range(0,101):
                            for h in range(0,201):
                                if a*values[0] + b *values[1] + c*values[2] + d*values[3] + e*values[4] + f*values[5] + g*values[6] + h*values[7] ==200:
                                    combos+=1
                                    print(combos,a,b,c,d,e,f,g,h)

#this will get it but it's very slow.