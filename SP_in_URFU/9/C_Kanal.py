for _ in range(int(input())):
    n, a, q = map(int, input().split())
    f = input()

    resx = a
    resl = a

    px = 0
    pl = 0
    # plus = 0
    # minus = 0

    for i in range(q):
        if resx >= n:
            px = 1
        if resl >= n:
            pl = 1

        if f[i] == '+':
            resx += 1
            resl += 1
        else:
            resx -= 1
    if resx >= n:
        px = 1
    if resl >= n:
        pl = 1

    if px + pl == 0:
        print('NO')
    elif px + pl == 1:
        print('MAYBE')
    else:
        print('YES')
    # if a >= n:
    #     print('YES')
    # else:
    #     if plus - minus < 0:
    #         resx = 0
    #     else:
    #         resx = 1 if a + plus - minus >= n else 0
    #     resl = 1 if a + plus >= n else 0
    #
    #
