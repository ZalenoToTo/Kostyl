n, m = map(int, input().split())
a = list(map(int, input().split()))[::-1]
if m >= max(a):
    print(n)
else:
    print(n - a.index(max(a)))

# while any(a):
#     for i in range(len(a)):
#         if a[i] < 1:
#             a[i] = 0
#             continue
#         a[i] -= m
#     res += 1
#
# print(res)
