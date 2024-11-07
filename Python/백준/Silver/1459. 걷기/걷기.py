def min_time_to_home(X, Y, W, S):
    # Case 1: 가로나 세로로만 이동하는 경우
    # 가로, 세로로만 이동할 때는 (X + Y) 번 이동이 필요하며, 각 이동당 시간은 W
    case1 = (X + Y) * W

    # Case 2: 대각선으로 최대한 이동하고 나머지는 가로나 세로로 이동하는 경우
    # 대각선으로 min(X, Y) 번 이동한 후, 나머지 차이는 가로나 세로로 이동
    # 이 경우 총 시간은 (min(X, Y) * S) + (|X - Y| * W)
    case2 = min(X, Y) * S + abs(X - Y) * W

    # Case 3: 대각선으로만 이동하는 경우
    # 대각선으로만 이동해서 정확히 도달하려면 X와 Y의 차이가 짝수여야 함
    # 그리고 대각선 이동이 더 효율적이어야 함 (S <= W)
    if (X + Y) % 2 == 0:
        case3 = max(X, Y) * S
    else:
        # 대각선 이동이 더 효율적이지만 X+Y가 홀수라 정확히 도달할 수 없는 경우
        # 최대한 대각선으로 이동한 후 마지막 한 칸을 가로나 세로로 이동
        case3 = (max(X, Y) - 1) * S + W

    # 최종적으로 세 가지 경우 중 최소값을 반환
    return min(case1, case2, case3)

x,y,w,s = map(int,input().split())
print(min_time_to_home(x,y,w,s))