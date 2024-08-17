def arr_dfs_recur(i, j, c=1, s=0, v=None):
    # i j좌표, c 남은 깎음 횟수, l 이전칸까지 등산로 길이, pre 이전 칸 높이
    global maxV
    if v == None : v = [[0]*N for _ in range(N)]
 
    if maxV < s+1: # 등산로 길이 갱신
        maxV = s+1
  
    v[i][j] = 1
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
            if arr[i][j]>arr[ni][nj]:
                arr_dfs_recur(ni, nj, c, s+1,v)
            elif c>0 and arr[i][j]>arr[ni][nj]-K:
                org = arr[ni][nj]
                arr[ni][nj] = arr[i][j] - 1
                arr_dfs_recur(ni, nj, 0, s+1,v) # 필요한만큼만 현재칸을 깎음
                arr[ni][nj] = org
    v[i][j] = 0
 
def find_highest(arr): # 최댓값이 여러개일때, 최댓값 인덱스?
    h_list = []
    # 1. 일단 최댓값을 찾고 2. 다시 돌려야 하나?
    # 최댓값
    max_val = max(map(max,arr))
    # 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_val : h_list.append((i,j))
    return h_list # [(0, 0), (2, 3), (2, 4)]
 
 
 
T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    maxV = 0
    for i,j in find_highest(arr) : arr_dfs_recur(i,j) 
    print(f"#{tc} {maxV}")