n, k = map(int, input().split())
a = list(map(int, input().split()))
m = min(a)
p = 0

for i in range(n):
    if (a[i] - m) % k != 0:
        print(-1)
        break
    p += a[i] - m
else:
    print(p // k)
