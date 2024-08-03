N = int(input()) # 1~30,000 중 양의 정수
max_num = 0

for i in range(1,N+1):
    ans = [N]
    n_1 = N
    next_n = i
    while next_n >= 0:
        ans.append(next_n)
        n_1 , next_n = next_n, n_1
        next_n -= n_1

    if len(ans) > max_num :
        max_num = len(ans)
        final_ans = ans


print(max_num)
print(*final_ans)