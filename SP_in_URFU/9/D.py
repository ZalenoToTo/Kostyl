for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = []

    for i in range(n):
        if a[i] - i != 0:
            res.append(abs(a[i] - i - 1))

    print(min(res))

    # mk = n
    # for i in range(n):
    #     if 0!=max(a[i]-1,i)- min(a[i]-1,i)<mk:
    #         mk = max(a[i]-1,i)- min(a[i]-1,i)
    # print(mk)