m,n = map(int,input().split())
row_list = [0,m]
col_list = [0,n]
N = int(input())
for _ in range(N):
    direction,cut_num = map(int,input().split())
    if direction == 0 : # 가로로 자름
        col_list.append(cut_num)
    else :              # 세로로 자름
        row_list.append(cut_num)
col_list.sort()
row_list.sort()

ans_list=[]
for i in range(len(col_list)-1) :
    for j in range(len(row_list)-1):
        ans_list.append((col_list[i+1] - col_list[i]) * (row_list[j+1] - row_list[j]))

print(max(ans_list))