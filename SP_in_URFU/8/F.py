x1, y1, x2, y2 = map(int, input().split())

if x1 - x2 == y1 - y2:
    print(x1, y2, x2, y1)
elif x1 == x2:
    a = abs(y1 - y2)
    print(x1 + a, y1, x2 + a, y2)
elif y1 == y2:
    a = abs(x1 - x2)
    print(x1, y1 + a, x2, y2 + a)
else:
    print(-1)
