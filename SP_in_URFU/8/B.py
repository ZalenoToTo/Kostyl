from math import inf

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    p = inf
    res = -1
    o = []
    for i in range(n):
        if a[i] < p:
            if a[i] in o:
                o.append(a[i])
            else:
                p = a[i]
                res = i
        # print(d)
        # if a[i] not in o:
        #     o.append(a[i])
        #     d[a[i]] = i + 1
        # elif a[i] in d:
        #     del d[a[i]]

    print(res)
    # print(d)
    # if len(d) == 0:
    #     print(-1)
    # else:
    #     print(d[min(d.keys())])

    # res = None
    #
    # for i in range(len(a)):
    #     p = a[i]
    #     if {p}.isdisjoint({a.pop(i)}):
    #         a.insert(i, p)
    #         if res is None:
    #             res = i
    #         elif a[res] > p:
    #             res = i
    #     else:
    #         a.insert(i, p)
    #
    # print(res)