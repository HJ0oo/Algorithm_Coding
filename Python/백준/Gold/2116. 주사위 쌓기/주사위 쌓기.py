N = int(input())
dice = []
for _ in range(N):    
    input_list = list(map(int,input().split()))
    one_of_dice = [input_list[0],input_list[5],input_list[1],input_list[3],input_list[2],input_list[4]]
    dice.append(one_of_dice)


# 결국 '하나의 dice에 남아있는 값 중 가장 큰 값' 들의 '합'이 가장 커야하는 것. 전체적인 합을 구하는 것은 의미가 없음
ans_list = [] # 첫번째 주사위에서 고르는 수에 따라 6개의 경우의 수가 나올 것

for start_index in range(6) :
    ans = 0
    remain = [1,2,3,4,5,6]                # 각 dice 에서 맨위와 맨아래를 remove로 지운 후,
    remain.remove(dice[0][start_index])

    if start_index % 2 == 0 :     # 0 2 4
        next_num = dice[0][start_index+1]
    else :                        # 1 3 5
        next_num = dice[0][start_index-1]
    remain.remove(next_num)
    ans += max(remain)                    # 남은 4개의 수 중 max 값을 ans에 더함

    for dice_num in range(1,N) :
        for i in range(6):
            if dice[dice_num][i] == next_num :
                remain = [1,2,3,4,5,6]
                remain.remove(next_num)
                if i % 2 == 0 : next_num = dice[dice_num][i+1]
                else : next_num = dice[dice_num][i-1]
                remain.remove(next_num)
                ans += max(remain)
                break
                
    ans_list.append(ans)                # N개의 주사위에 대해 모두 수행한 후의 ans 값
print(max(ans_list))                    # 6개의 경우의 수 중 max 값 출력




