# 더 생각해볼 코드
# N = int(input())
# total_list = []
# H_list = []
# for _ in range(N) :
#     L, H = map(int,input().split())
#     total_list.append([L,H])
# print(total_list)
# total_list.sort() # 첫 번째 값 기준으로 sort되나봥
# print(total_list)

N = int(input())
total_list = [0] * 1001
for _ in range(N):
    L, H = map(int, input().split())
    total_list[L] = H

standard_index = total_list.index(max(total_list)) # 제일 높은 거 기준으로 삼고

now_max = 0
for i in range(0,standard_index) :          # 기준 왼쪽 부분 - 0 ~ standard_index-1 까지
    if now_max <= total_list[i] :
        now_max = total_list[i]
        total_list[i] = now_max
    else :
        total_list[i] = now_max

now_max = 0
for i in range(1000,standard_index,-1) :    # 기준 오른쪽 - 1000 ~ standard_index+1 까지
    if now_max <= total_list[i] :
        now_max = total_list[i]
        total_list[i] = now_max
    else :
        total_list[i] = now_max

# print(total_list) # [0, 0, 4, 4, 6, 6, 6, 6, 10, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, ...]
print(sum(total_list))