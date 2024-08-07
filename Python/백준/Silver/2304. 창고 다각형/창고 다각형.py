# N = int(input())
# total_list = []
# H_list = []
# for _ in range(N) :
#     L, H = map(int,input().split())
#     total_list.append([L,H])
#
# print(total_list)
# total_list.sort() # 첫 번째 값 기준으로 sort되나봥
#
# print(total_list)

N = int(input())
total_list = [0] * 1001
for _ in range(N):
    L, H = map(int, input().split())
    total_list[L] = H
#
# print(total_list)
# print(max(total_list))
# print(total_list.index(max(total_list)))

standard_index = total_list.index(max(total_list))
# for m in range(standard_index-1,-1,-1): # standard_index-1 ~ 0
#     pass
# for m in range(standard_index,-1,-1): # standard_index+1 ~ 0
#     pass

now_max = 0
for i in range(0,standard_index) :
    if now_max <= total_list[i] :
        now_max = total_list[i]
        total_list[i] = now_max
    else :
        total_list[i] = now_max
# print(total_list)
# print("ddd")
# print(len(total_list))

now_max = 0
for i in range(1000,standard_index,-1) :
    if now_max <= total_list[i] :
        now_max = total_list[i]
        total_list[i] = now_max
    else :
        total_list[i] = now_max

# print(total_list)
print(sum(total_list))