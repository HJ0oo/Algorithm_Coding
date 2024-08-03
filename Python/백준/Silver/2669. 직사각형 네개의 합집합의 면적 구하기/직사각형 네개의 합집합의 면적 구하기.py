left_1_x,left_1_y,right_1_x,right_1_y = map(int, input().split())
left_2_x,left_2_y,right_2_x,right_2_y = map(int, input().split())
left_3_x,left_3_y,right_3_x,right_3_y = map(int, input().split())
left_4_x,left_4_y,right_4_x,right_4_y = map(int, input().split())

cnt = 0
on_list=[[0] * 101 for _ in range(101)]
def rect(left_x,left_y,right_x,right_y):
    global cnt
    for i in range(left_x,right_x):
        for j in range(left_y,right_y):
            if on_list[i][j] == 0 :
                on_list[i][j] = 1
                cnt += 1

rect(left_1_x,left_1_y,right_1_x,right_1_y)
rect(left_2_x,left_2_y,right_2_x,right_2_y)
rect(left_3_x,left_3_y,right_3_x,right_3_y)
rect(left_4_x,left_4_y,right_4_x,right_4_y)

print(cnt)