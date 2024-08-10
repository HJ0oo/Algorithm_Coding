# 재귀 함수 활용 - 팩토리얼 재귀 구현처럼.
def recur(num1,num2):
    if num1-num2 < 0 : # 종료 조건
        return [num1,num2]
    return [num1]+recur(num2,num1-num2)

'''
예시
print(recur(100,62))
[100, 62, 38, 24, 14, 10, 4, 6]
'''


N = int(input())        # 첫번째 수 N = 1~30,000 중 양의 정수
max_len = -1
for i in range(1,N+1) : # 두번째 수는 1~N까지 가능
    new_ans = recur(N,i)
    if max_len < len(new_ans):
        ans = new_ans
        max_len = len(new_ans)

print(max_len)
print(*ans)