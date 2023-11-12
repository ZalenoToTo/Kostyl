for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    p = a[0]
    ch = 0

    for j in a:
        if j % 2 == 0:
            ch += 1

    if ch % 2 == 0:
        for q in range(1, n * 2):
            if p % 2 == a[q] % 2:
                a[q] = 0
                a[0] = 0
                break
    else:
        for q in range(1, n * 2):
            if p % 2 != a[q] % 2:
                a[q] = 0
                a[0] = 0
                break
    for i in range(n * 2):
        if a[i] == 0:
            continue
        for j in range(n * 2):
            if j != i and a[j] != 0 and a[i] % 2 == a[j] % 2:
                print(i + 1, j + 1)
                a[j] = 0
                a[i] = 0
                break
