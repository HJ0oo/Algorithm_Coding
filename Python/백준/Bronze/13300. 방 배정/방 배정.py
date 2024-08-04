N, K = map(int,input().split())
total_student = [ [0] * 2 for _ in range(6) ]
for _ in range(N) :
    S, Y = map(int,input().split())
    total_student[Y-1][S] += 1

ans = 0
for grade in total_student:
    for s in grade:
        ans += (s+1) // 2
print(ans)