x, y, z = map(int, input().split())
a, b, c = map(int, input().split())
a -= x

if a + b >= y and a + b - y + c >= z and a > -1:
    print('YES')
else:
    print('NO')
