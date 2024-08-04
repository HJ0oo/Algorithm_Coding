# 9개 중 7개를 선택하는 조합 반환 - 재귀함수 사용
def combinations(arr,start=0,current_combination=[],current_sum=0):
    if len(current_combination) == 7:
        if current_sum == 100:
             return [current_combination]
        else :
            return []
    if start >= len(arr):
            return []
    with_current = combinations(arr,start+1,current_combination+[arr[start]],current_sum+arr[start])
    without_current = combinations(arr, start + 1, current_combination, current_sum)

    return with_current + without_current

input_list = []
for _ in range(9) :
    input_list.append(int(input()))

ans_list = combinations(input_list)
# print(ans_list)
ans_list[0].sort()
for z in ans_list[0]:
    print(z)