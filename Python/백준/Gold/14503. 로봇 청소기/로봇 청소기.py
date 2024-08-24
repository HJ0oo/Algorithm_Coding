import pprint
def clean(i,j,direction):
    global arr
    global real_cnt
    
    # print(i,j,direction)
    # 지금 있는 위치 i j, 지금 direction
    # 8 5 0 에서 잘못돌아간것
    # 8 6 1 이 되어야 함
    if not(0<=i<N) or not(0<=j<M) or arr[i][j]==1 :
        return

    arr[i][j] = -1 # 청소한 칸
    real_cnt += 1

    find_next_direction = (direction + 3) % 4 # 반시계 회전
    # print("next_d",find_next_direction)
    for _ in range(4) :
        if arr[i+direction_list[find_next_direction][0]][j+direction_list[find_next_direction][1]] == 0 :
            # print("direc",find_next_direction)
            direction = find_next_direction
            i += direction_list[find_next_direction][0]
            j += direction_list[find_next_direction][1]
            clean(i,j,direction)
            break
        else :
            find_next_direction = (find_next_direction + 3) % 4
    else:
        # 바라보는 방향을 유지한 채로 한 칸 "후진할 수 있다면"
        # 한 칸 후진하고 1번으로 돌아간다.
        # print("last",direction)
        i -= direction_list[direction][0]
        j -= direction_list[direction][1]
        # print("i,j",i,j,direction)
        # pprint.pprint(arr)
        if 0<=i<N and 0<=j<M and arr[i][j]!=1 :
            clean(i,j,direction)
        else :
            # 작동 끝
            return


    return

north = 0   # (-1,0)
east = 1    # (0,1)
south = 2   # (1,0)
west = 3    # (0,-1)
# 반시계방향으로 회전 시
# n > w > s > e > n ... 0>3>2>1>0...
direction_list = [(-1,0),(0,1),(1,0),(0,-1)]


N, M = map(int,input().split())
r,c,direction = map(int,input().split())
arr = [ list(map(int,input().split())) for _ in range(N) ]
real_cnt = 0
first_one_cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 : first_one_cnt += 1
clean(r,c,direction)

# pprint.pprint(arr)
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 : cnt += 1
print(N*M - first_one_cnt - cnt)
# print(real_cnt)
# print("끝")