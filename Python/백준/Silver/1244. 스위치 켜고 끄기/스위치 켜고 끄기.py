N = int(input())
arr = [0] + list(map(int,input().split())) # index와 스위치 번호 일치시키기위해 [0] 추가
stu_num = int(input()) # 0,1 과 '0','1' 잘 체크하기
for _ in range(stu_num):
    s, switch_num = map(int,input().split())
    if s == 1 : # 남학생 - 배수
        k = 1
        multi = switch_num
        while multi <= N :
            if arr[multi] == 1 :
                arr[multi] = 0
            else :
                arr[multi] = 1
            k += 1
            multi = k * switch_num # 이전코드처럼 += 로 하면 5,10,20,30..

    else :      # 여학생 - 대칭 체크
        change_i = 0
        # print(arr)
        for i in range(1,N):
            if switch_num-i <= 0 or switch_num+i >= N+1 : # 경계값 설정
                break
            if arr[switch_num - i] == arr[switch_num + i] : # 대칭이라면 연속적으로.
                change_i = i
            else :  # 좌우 대칭 안맞다면 break
                break
        # print("change_i",change_i)

        for index in range(switch_num-change_i,switch_num+change_i+1):
            # print("여기부터 여기까지 변경",switch_num-change_i,switch_num+change_i)
            if arr[index] == 1 : arr[index] = 0
            else : arr[index] = 1

# 이진법 활용해서 한번에 바꾸는 방법도 있을것같은데
# 1111 = 1010 + 0101

ans = arr[1:]
# 20개씩 출력
for i in range(len(ans)): # 21개라면 i는 0~20 - 19과 20 사이에 print()
    print(ans[i],end=" ")
    if i % 20 == 19 :
        print()