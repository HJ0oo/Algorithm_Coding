from collections import deque

T = 10
for tc in range(1, T + 1):

    ans_list = []
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    print(f'#{tc}', end=' ')
    adjl = [[] for _ in range(V+1)]
    adjl2 = [0] * (V+1)

    for i in range(0,2*E,2):
        adjl[arr[i]].append(arr[i+1])
        adjl2[arr[i+1]] += 1

    # print(adjl)
    # print(adjl2)
    '''
    [[], [2, 5], [3, 7], [], [1], [6], [], [6], [5, 9], []]
    [0, 1, 1, 1, 0, 2, 2, 1, 0, 1]
    '''
    # 진입차수가 0인 정점이 아예 없을 수는 없음

    q = deque()
    visited = [0] * (V+1)
    for i in range(1,V+1):
        if adjl2[i] == 0 :
            q.append(i)
            visited[i] = 1
    while q :
        t = q.popleft()
        print(t, end=' ')
        for i in adjl[t] :
            adjl2[i] -= 1
            if adjl2[i] == 0 :
                q.append(i)
                visited[i] = visited[t] + 1
    print()
    