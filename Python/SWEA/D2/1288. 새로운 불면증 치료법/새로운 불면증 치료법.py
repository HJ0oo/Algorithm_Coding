T = int(input())
for tc in range(1,T+1):
    cnt = 1
    N = int(input())
    check = 0                   # 0 ~ 9 까지의 모든 숫자 - 비트마스크 0000000000 이라고 생각.
    multi = N
    while check < 2**10 - 1 :   # 1111111111 이 될 때까지. = 2**N - 1
        for s in str(multi) :
            check = check | (1<<int(s))
        multi += N

    print(f"#{tc} {multi - N}")