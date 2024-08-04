N = int(input())
ans_list = [0] * N
# 방법 1 - 0 행렬 만들어서 직접 색칠
total_arr = [[0] * 1002 for _ in range(1002)]
for paper_num in range(1,N+1):

    left_x,left_y,length,height = map(int, input().split())
    right_x = left_x + length
    right_y = left_y + height

    for i in range(left_x,right_x):
        for j in range(left_y,right_y):
            total_arr[i][j] = paper_num

for paper_num in range(1,N+1) :
    for i in range(1002):
        for j in range(1002):
            if total_arr[i][j] == paper_num :
                ans_list[paper_num-1] += 1

for p in ans_list:
    print(p)
