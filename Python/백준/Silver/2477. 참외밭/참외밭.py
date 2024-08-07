K = int(input())
total_list = []
garo_list = []
sero_list = []
for _ in range(6):
    direction,length = map(int,input().split())
    if direction == 1 or direction == 2 :
        garo_list.append(length)
    else :
        sero_list.append(length)
    total_list.append([direction,length])
total_list.append(total_list[0]) # 꼼수로 해결@
total_list.append(total_list[1]) # 꼼수로 해결@
total_list.append(total_list[2]) # 꼼수로 해결@
# print(total_list)

for i in range(0,6): # 0~5
    if total_list[i][0] == total_list[i+2][0] and total_list[i+1][0] == total_list[i+3][0]:
        ans = total_list[i+1][1] * total_list[i+2][1]
        break

# print(ans)
# print(max(garo_list))
# print(max(sero_list))
print((max(garo_list) * max(sero_list) - ans) * K)

