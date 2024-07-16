# 2635
first_num = int(input())                #입력값이 1일 때
ans_list=[]                             #ans_list=[]
num_list=[]                             #num_list=[]

def minus(i,j):
    if((i-j)>=0):
        num_list.append(i-j)
        return minus (j,i-j)


for sec_num in range (1,first_num+1):   #1
    num_list=[first_num]                #num_list=[1]
    num_list.append(sec_num)            #num_list=[1,1]
    minus(first_num,sec_num)            # .. num_list=[1,1,0,1]
    ans_list.append(num_list)           #ans_list=[[1,1,0,1]]


max_len = 0                             #max_len=0



if(len(ans_list)!=1):
    for i in range(len(ans_list)-1):        #range(0,0)
        if max_len < len(ans_list[i]):
            max_len = len(ans_list[i])
            ans = i
else:                                       #input이 1일 때 오류 해결; len(ans_list)=1 일 때.
    max_len=len(ans_list[0])
    ans=0


print(max_len)

for i in ans_list[ans]:
    print(i,end=' ')