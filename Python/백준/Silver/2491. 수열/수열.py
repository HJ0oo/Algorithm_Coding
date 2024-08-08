N = int(input())
arr = list(map(int, input().split()))
ans_list = []
# 그냥 앞뒤로 한번씩 하면... 시간 초과가 뜰까..?
length = 1
for i in range(0, N-1):
    if arr[i] <= arr[i+1]:
        length += 1
    else:
        if length != 1:
            ans_list.append(length)
        length = 1
else :
    ans_list.append(length)
# print(ans_list)

arr.reverse()

length = 1
for i in range(0, N-1):
    if arr[i] <= arr[i+1]:
        length += 1
    else:
        if length != 1:
            ans_list.append(length)
        length = 1
else :
    ans_list.append(length)

# print(ans_list)
print(max(ans_list))

# 주어진 코드에서 런타임 에러의 주요 원인은 ans_list가 비어 있을 때 max(ans_list)를 호출하기 때문입니다.
# max() 함수는 빈 리스트에서 호출될 때 에러를 발생시킵니다.
# 따라서, 코드 실행 중 ans_list가 비어 있을 가능성을 고려하지 않았기 때문에 문제가 발생합니다.
# 이를 해결하기 위해서는 ans_list가 비어 있지 않은지 확인하고, 비어 있을 경우 적절한 기본값을 반환하도록 해야 합니다.
