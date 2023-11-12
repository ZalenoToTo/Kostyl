for _ in range(int(input())):
    n = int(input())
    res = 0
    sv_vol = 0
    not_prov_svin = 0
    b = list(map(int, input().split()))

    for i in range(n):
        if b[i] == 1:
            if sv_vol > 0:
                sv_vol -= 1
            else:
                res += 1
            not_prov_svin += 1
        else:
            if not_prov_svin % 2 == 1:
                sv_vol += (not_prov_svin - 1) // 2
            else:
                sv_vol += (not_prov_svin - 2) // 2
            not_prov_svin = 0
    print(res)