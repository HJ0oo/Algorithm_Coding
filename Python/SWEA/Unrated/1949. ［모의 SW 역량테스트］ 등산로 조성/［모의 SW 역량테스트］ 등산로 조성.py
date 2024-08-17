def arr_dfs_recur(i, j, cut=False, s=0, visited=None):
    # i j좌표, cut 깎았다면 True 안깎았다면 False, S 이전칸까지 등산로 길이
    global maxV
    if visited == None : visited = [[False]*N for _ in range(N)]
 
    if maxV < s+1: # 등산로 길이 갱신
        maxV = s+1
  
    # 현재 위치 방문 표시
    visited[i][j] = True

    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj     # 새로운 위치 ni,nj

        # 배열 범위 내 + 방문 하지 않은 곳 있다면!
        if 0<=ni<N and 0<=nj<N and visited[ni][nj]==False:
            # 1. 값이 더 작다면 이동!
            if arr[i][j] > arr[ni][nj]:
                arr_dfs_recur(ni, nj, cut, s+1, visited) ##### 여기에 cut이 아니라 False를 넣어서 오답 - 당연. cut = True 된 이후에도 재귀 호출로 이 함수 쓸텐데!
                                
            # 2. 그렇지 않더라도, 깎지 않은 상태에서 K를 줄이고 갈 수 있다면 이동!
                '''(2,3) 9 (2,4) 9 일때'''
            elif cut == False and arr[i][j] > arr[ni][nj] - K:
                # 2-1 나중에 원상복구 위해 새로운 위치의 높이를 저장
                original_height = arr[ni][nj]
                
                # 2-2 지형 깎음
                ''' (2,4) 8로 깎고'''
                arr[ni][nj] = arr[i][j] - 1
                
                # 2-3 깎은 상태로 이동(cut을 True로 설정하여 다시 깎을 수 없도록)
                ''' arr_dfs_recur(2, 4, True, s+1, visited) 호출 '''
                arr_dfs_recur(ni, nj, True, s+1, visited)
                ''' 호출 끝까지 가면 그냥 해당 visited = True 됐다가 다시 False 된 것 '''
                ''' 그냥 원래대로 돌아온 상태. 깎은 상태에서의 경로 파악 완료. '''
                
                # 2-4 원상복구(다른 경로 탐색을 위해)
                arr[ni][nj] = original_height

    '''
    (2, 3)로 돌아와서 복구한 후, 다른 방향으로 경로를 탐색
    원래였으면 못갈 곳을 elif에서 해봤던 거고, 이제는 원래대로!
    예를 들어, (3, 3)로 이동 (arr[3][3] = 7).
    '''
    # 탐색이 끝나면 현재 위치를 다시 방문 가능하도록 설정 (백트래킹)
    visited[i][j] = False


    
def find_highest(arr): # 최댓값이 여러개일때, 최댓값 인덱스 반환
    h_list = []
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