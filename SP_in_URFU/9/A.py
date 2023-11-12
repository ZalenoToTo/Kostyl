for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = a[::-1]
    jc = {str(b[0]): b.count(b[0])}
    p = n
    for i in range(1, n):
        if b[i] <= b[i - 1]:
            if not (jc.get(str(b[i]))):
                jc[str(b[i])] = b.count(b[i])
        else:
            p = i
            break
    res = 0
    for i in range(p):
        # print(jc)
        if jc[str(b[i])] != b[0:p].count(b[i]):
            res = len(set(b[i:n]))
            break
    else:
        res = len(set(b[p:n]))