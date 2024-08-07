import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
now = max_sum = sum(arr[0:0+K])
for i in range(1,N-K+1) : #1~N-K
    now = now - arr[i-1] + arr[i+K-1]
    if max_sum <= now :
        max_sum = now
print(max_sum)