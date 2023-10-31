for _ in range(int(input())):
    n = int(input()) # 5
    a = list(map(int, input().split())) # 2 1 3
    sa = sorted(a) # 1 2 3
    c = 1
    la = sa[0] # 1
    #i = 1
    f = 0
    for i in range(1, n):
        if la == sa[i]: # False
            c+=1
        else:
            if c==1: # True
                f = 1
                break
            else:
                if i==n-1: # False
                    f = 2
                    break
                else:
                    c = 1
                    la = sa[i] 
    if f ==1:
        print(a.index(la)+1)# a.index(1+1)
    elif f == 2:
        print(a.index(sa[-1])+1)
    elif n == 1:
        print(a[0])
    else:
        print(-1)
