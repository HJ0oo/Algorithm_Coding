# 9개 중 7개를 선택하는 조합 반환
# 방법 1 - 재귀함수 사용
def combinations_recur(arr,start_index=0,current_combination=[],current_sum=0):
    if len(current_combination) == 7 :      # 7개 조합
        if current_sum == 100 :             # 합이 100이면 끝
             return [current_combination]
        else :                              # 100이 아니라면 다시.
            return []
    
    if start_index >= len(arr):
            return []
    with_current = combinations_recur(arr,start_index+1,current_combination+[arr[start_index]],current_sum+arr[start_index])
    without_current = combinations_recur(arr, start_index + 1, current_combination, current_sum)

    return with_current + without_current

input_list = []
for _ in range(9) :
    input_list.append(int(input()))

ans_list = combinations_recur(input_list)
ans_list[0].sort() # 문제 조건에서 불가능한 경우는 없다고 했으니까 그냥 첫번째 값 가져옴
for z in ans_list[0]:
    print(z)




# # 방법 2 - 반복문 사용
# def find_combinations_iterative(arr, k, target_sum):
#     result = []
#     stack = [(0, [], 0)]  # (현재 인덱스, 현재까지의 조합, 현재까지의 합)

#     while stack:
#         start, current_combination, current_sum = stack.pop()
#         if len(current_combination) == k:
#             if current_sum == target_sum:
#                 result.append(current_combination)
#             continue
        
#         if start >= len(arr):
#             continue
        
#         # Include the current element
#         if current_sum + arr[start] <= target_sum:
#             stack.append((start + 1, current_combination + [arr[start]], current_sum + arr[start]))
        
#         # Exclude the current element
#         stack.append((start + 1, current_combination, current_sum))
    
#     return result

