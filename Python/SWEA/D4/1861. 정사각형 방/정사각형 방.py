def move(i,j) :
    global visited, cnt
    visited[i][j] = 1
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] + 1:
            cnt += 1
            move(ni,nj)
            break  # 동일한 수가 없기 때문


# 파이썬 1초 - 3천만 정도

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [ list(map(int,input().split())) for _ in range(N) ]
    visited = [[0] * N for _ in range(N)]
    # 출발지 미정 - 이차원 리스트 한번은 순회해야함 (1 ≤ N ≤ 10^3) N^2
    max_move_cnt = -1
    room_num = -1
    for i in range(N):
        for j in range(N):
            if visited[i][j] ==0 :
                cnt = 0
                move(i,j)
                if max_move_cnt < cnt :
                    max_move_cnt = cnt
                    room_num = arr[i][j]
                elif max_move_cnt == cnt:
                    room_num = min(room_num,arr[i][j])

    print(f"#{tc} {room_num} {max_move_cnt+1}")