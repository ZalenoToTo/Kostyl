for i in range(int(input())):
    a, k = map(int, input().split())

    if (a == 1 or a == 2) and k > 0:
        print(-1)
        continue

    if (a - 1) // 2 < k:
        print(-1)
        continue

    m = list(range(1, a + 1))
    r, s = m[:a - k], m[a - k:]
    c1 = 0
    c2 = 0

    try:
        for i in range(a):
            if i % 2 == 0:
                print(r[c1], end=' ')
                c1 += 1
            else:
                print(s[c2], end=' ')
                c2 += 1
    except Exception as e:
        print(*r[c1:], end=' ')

    print()
