p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(p[4:7])
for _ in range(int(input())):
    l, r = input().split()
    res = 0

    for i in range(len(r)):
        res += abs(min(p[min(int(l[i]), int(r[i]) + 1):max(int(r[i]) + 1, int(l[i]))]) - max(p[min(int(l[i]), int(r[i]) + 1):max(int(r[i]) + 1, int(l[i]))]))
    print(res)