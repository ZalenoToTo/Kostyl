for _ in range(int(input())):
    n = int(input())
    s = n // 2 + 1
    res = 0

    for i in range(1, n):
        res += ((n - i + 1) * 4 - 4) * (s - i)

    print(res)
