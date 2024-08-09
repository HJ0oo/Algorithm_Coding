
# 방법 1 - 0 행렬 만들어서 직접 색칠
import sys
N = int(sys.stdin.readline().rstrip())
ans_list = [0] * N
total_arr = [[0] * 1002 for _ in range(1002)]

for paper_num in range(1,N+1):
    left_x,left_y,length,height = map(int, sys.stdin.readline().rstrip().split())
    right_x = left_x + length
    right_y = left_y + height

    for i in range(left_x,right_x):
        for j in range(left_y,right_y):
            total_arr[i][j] = paper_num

# # 기존 코드 - 색종이 개수 만큼 for문을 더 돌림
# for paper_num in range(1,N+1) :
#     for i in range(1002):
#         for j in range(1002):
#             if total_arr[i][j] == paper_num :
#                 ans_list[paper_num-1] += 1
# 배열 탐색을 한 번만 수행하여 각 색종이의 넓이 계산
for i in range(1002):
    for j in range(1002):
        if total_arr[i][j] != 0:  # 0이 아닌 경우, 즉 색종이가 덮고 있는 경우
            ans_list[total_arr[i][j] - 1] += 1

for p in ans_list:
    print(p)