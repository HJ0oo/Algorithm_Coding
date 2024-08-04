N = int(input())
arr = list(map(int,input().split()))
ans_list = []
stu_num = 1
for pick_num in arr :
    ans_list.insert(len(ans_list)-pick_num,stu_num)
    stu_num += 1
print(* ans_list)