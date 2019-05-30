def main():
    ps = set() ## not my code. I had the same idea, but using list instead of set. List very slow. Set fast.
    i = 1
    while True:
        i += 1
        s = (3 * i * i - i) // 2
        for Pj in ps:
            if s - Pj in ps and s - 2 * Pj in ps: # s = sum. Pj = num1. Pk = num 2. s- Pj == Pk. s -2Pj ==Pk - Pj == difference!
                return s - 2 * Pj
        ps.add(s)


if __name__ == '__main__':
    print(main())