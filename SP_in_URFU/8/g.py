for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    p = 1

    for i in range(1, n):
        if a[i] > a[i - 1]:
            for j in range(n):
                if a[i] > a[j] > a[i - 1]:
                    p += 1
                    break

        else:
            p += 1

    if k >= p:
        print('YES')
    else:
        print('NO')
