# 별, 동그라미, 네모, 세모를 각각 숫자 4, 3, 2, 1로 표현한다

N = int(input()) # 첫 번째 줄에는 딱지놀이의 총 라운드 수를 나타내는 자연수 N이 주어진다. N 은 1 이상 1,000 이하이다.
for _ in range(N) : 
    a_list = list(map(int,input().split())) # 다음 줄에는 라운드 1에서 어린이 A가 내는 딱지에 나온 그림의 총 개수 a가 주어진다. a는 1 이상 100 이하이다
    a = a_list.pop(0)   # "뒤따라 나오는" a개의 정수는 어린이 A가 낸 딱지의 그림을 나타내는데, 각각 4, 3, 2, 1 중 하나의 값이다. 4, 3, 2, 1의 순서대로 주어지지 않을 수 있음에 주의하라. 
    b_list = list(map(int,input().split()))
    b = b_list.pop(0)

    a_result = {1:0,2:0,3:0,4:0}
    b_result = {1:0,2:0,3:0,4:0}
    for one_of_list in a_list :
        if one_of_list == 4 : a_result[4] += 1
        elif one_of_list == 3 : a_result[3] += 1
        elif one_of_list == 2 : a_result[2] += 1
        else : a_result[1] += 1
    # print(a_result)
    for one_of_list in b_list :
        if one_of_list == 4 : b_result[4] += 1
        elif one_of_list == 3 : b_result[3] += 1
        elif one_of_list == 2 : b_result[2] += 1
        else : b_result[1] += 1
    # print(b_result)

    for i in range(4,0,-1): #4부터 1까지 역순
        if a_result[i] > b_result[i] :
            ans = 'A'
            break
        elif a_result[i] < b_result[i] :
            ans = 'B'
            break
        else :
            ans = 'D'
            continue
    print(ans) # 각 라운드의 결과는 A가 승자라면 A, B가 승자라면 B, 무승부라면 D이다.