def bfs(box, ripe_tomatoes, M, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = ripe_tomatoes[:]
    days = 0

    while queue:
        new_queue = []
        for x, y in queue:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                    box[nx][ny] = 1
                    new_queue.append((nx, ny))
        if new_queue:  # new_queue가 비어 있지 않은 경우에만 days 증가
            days += 1
        queue = new_queue

    # 익지 않은 토마토가 있는지 확인
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1

    return days

def solution():
    M, N = map(int, input().split())
    box = []
    ripe_tomatoes = []
    
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            if row[j] == 1:
                ripe_tomatoes.append((i, j))
        box.append(row)

    days_needed = bfs(box, ripe_tomatoes, M, N)
    print(days_needed)

solution()