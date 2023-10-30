n = int(input())
m = list(map(int, input().split()))
res = 1

for i in range(len(m)):
    p = 1
    for j in range(i + 1, len(m)):
        if m[j] <= m[j - 1]:
            p += 1
        else:
            break
    if i != 0:
        for u in range(i, 0, -1):
            if m[u] >= m[u - 1]:
                p += 1
            else:
                break

    if p > res:
        res = p

print(res)