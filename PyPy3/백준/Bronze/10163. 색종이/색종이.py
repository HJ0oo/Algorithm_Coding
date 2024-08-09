# 방법 2 - 시간초과.
N = int(input())
final_dic = {}
final_list = [0] * N # 색종이별 최종 값을 담을 리스트

for k in range(N):
    left_x, left_y, length, height = map(int, input().split())
    right_x = left_x + length
    right_y = left_y + height
    for i in range(left_x,right_x):
        for j in range(left_y,right_y):
            final_dic[(i,j)] = k # 딕셔너리 어차피 key-value 하나니까 뒤에 입력값으로 덮어쓰기

for key in final_dic :
    final_list[final_dic[key]] += 1

for ans in final_list :
    print(ans)