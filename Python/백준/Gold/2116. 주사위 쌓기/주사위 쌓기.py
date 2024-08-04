N = int(input())
dice = []
for _ in range(N):    
    input_list = list(map(int,input().split()))
    one_of_dice = [input_list[0],input_list[5],input_list[1],input_list[3],input_list[2],input_list[4]]
    dice.append(one_of_dice)
    
# print(dice)

# 결국 '하나의 dice에 남아있는 값 중 가장 큰 값' 들의 '합'이 가장 커야하는 것. 전체적인 합을 구하는 것은 의미가 없음
ans_list = [] # 6개의 경우의 수가 나올 것

for start_index in range(6) :
    ans = 0
    remain = [1,2,3,4,5,6]
    remain.remove(dice[0][start_index])
    ################## sum_of_updown = 0
    ################## sum_of_updown += dice[0][start_index] #print(dice[0][start_index],"start")

    if start_index % 2 == 0 :   # 0 2 4
        next_num = dice[0][start_index+1]
    else :                  # 1 3 5
        next_num = dice[0][start_index-1]
    remain.remove(next_num)
    ans += max(remain)
    ################## sum_of_updown += next_num #print(next_num,"start")

    for dice_num in range(1,N) :
        for i in range(6):
            # print(dice_num,"dice_num")
            if dice[dice_num][i] == next_num :
                remain = [1,2,3,4,5,6]
                remain.remove(next_num)
                ################## sum_of_updown += next_num #print(i,next_num,"find same thing")
                if i % 2 == 0 : next_num = dice[dice_num][i+1]
                else : next_num = dice[dice_num][i-1]
                remain.remove(next_num)
                ################## sum_of_updown += next_num #print(dice_num,next_num,"next_num")
                ans += max(remain)
                break

    # print("ennd")
    # print(ans)
    ans_list.append(ans)
print(max(ans_list))




