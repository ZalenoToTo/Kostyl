for _ in range(int(input())):
    s = input()
    t = input()

    if t == 'abc':
        a1 = 0
        b1 = 0
        c1 = 0
        p = ''

        for i in s:
            if i == 'a':
                a1 += 1
            elif i == 'b':
                b1 += 1
            elif i == 'c':
                c1 += 1
            else:
                p += i

        if a1 == 0 or b1 == 0 or c1 == 0:
            print(''.join(sorted(s)))
            continue

        print('a' * a1 + 'c' * c1 + 'b' * b1 + ''.join(sorted(p)))
    else:
        print(''.join(sorted(s)))
