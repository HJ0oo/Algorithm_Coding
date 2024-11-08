from collections import deque
def bfs(start_i) :
    global visited
    q = deque([start_i])
    visited[start_i] = 1
    while q :
        for j in range(n):
            if j != start_i and computers[start_i][j] == 1 and visited[j] == 0 :
                q.push(j)
                visited[j] = 1
        
    
    
def solution(n, computers):
    answer = 0
    visited = [0] * (n)
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1 and visited[i] == 0: # i에서 출발, 같은 네트워크면 싹 바꿀것
                # bfs(i)
                #####
                q = deque([i])
                visited[i] = 1
                while q :
                    now_i = q.pop()
                    for j in range(n):
                        if j != now_i and computers[now_i][j] == 1 and visited[j] == 0 :
                            q.append(j)
                            visited[j] = 1
                #####
                
                answer += 1
    # print(n - sum(visited))
    answer += (n - sum(visited))
            
    # 네트워크가 아예 없는 경우 - 연결안되면 그거 자체로 네트워크임. if문 안돌아가니까 0
    # 컴퓨터가 1일 때 - if문 안돌아가니까 0
    return answer