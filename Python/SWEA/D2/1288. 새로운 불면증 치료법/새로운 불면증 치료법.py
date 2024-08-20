T = int(input())
for tc in range(1,T+1):
    cnt = 1
    N = int(input())
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    while num_list:
        multi_str = cnt * N
        for s in str(multi_str):
            if s in num_list :
                num_list.remove(s)
        cnt += 1

    print(f"#{tc} {N * (cnt-1)}")