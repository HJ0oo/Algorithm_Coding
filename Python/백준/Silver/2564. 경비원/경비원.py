def direc_distan(direc,distan):
    if direc == 1 :         # 북
        return [1,0,distan]
    elif direc == 2 :       # 남
        return [2,sero,distan]
    elif direc == 3 :       # 서
        return [3,distan,0]
    elif direc == 4 :       # 동
        return [4,distan,garo]

garo, sero = map(int,input().split())
store_num = int(input())
gps_list = []
for _ in range(store_num) :
    direc, distan = map(int,input().split())
    gps_list.append(direc_distan(direc,distan))

direc, distan = map(int,input().split())
user = direc_distan(direc, distan)

total = (garo + sero) * 2
ans_list = []
for gps in gps_list:
    if [user[0], gps[0]] in [[1,2],[2,1],[3,4],[4,3]] :
        ans = (user[1] + user[2] + gps[1] + gps[2])
        # print(ans)
        if ans <= total - ans :
            ans_list.append(ans)
        else :
            ans_list.append(total - ans)
    else :
        ans = abs(user[1] - gps[1]) + abs(user[2] - gps[2])
        # print(ans)
        if ans <= total - ans :
            ans_list.append(ans)
        else :
            ans_list.append(total - ans)
    
# print(ans_list)
print(sum(ans_list))

