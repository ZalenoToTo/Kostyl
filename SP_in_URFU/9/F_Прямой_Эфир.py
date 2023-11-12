for _ in range(int(input())):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    pe = [j for j in range(1, n + 1)]
    res = {}

    for i in range(m):
        try:
            pe.pop(pe.index(p[i]))
            pe.insert(0, p[i])
        except ValueError:
            res[pe.pop(-1)] = i + 1
            pe.insert(0, p[i])

    for k in range(1, n + 1):
        try:
            print(res[k], end=' ')
        except KeyError:
            print(-1, end=' ')
    print()
