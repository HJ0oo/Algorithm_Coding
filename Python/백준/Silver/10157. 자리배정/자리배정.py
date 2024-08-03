C, R = map(int,input().split())
K = int(input())

def find(C,R) :
    # 세로 C (j) * 가로 R (i) 배열로 생각, 왼쪽 가장 위에서 시작 (1,1)이라고 생각.
    arr = [[0] * R for _ in range(C)]

    di = [0,1,0,-1] # 델타 활용
    dj = [1,0,-1,0]

    ni = nj = -1
    num = 1

    for _ in range((C+1)//2) :
        for k in range(4):
            ni -= di[k-1]
            nj -= dj[k-1]
            ni += di[k]
            nj += dj[k]
            while 0 <= ni < C and 0 <= nj < R and arr[ni][nj] == 0 :
                if num == K :
                    return ni+1,nj+1
                arr[ni][nj] = num
                ni += di[k]
                nj += dj[k]
                num += 1

if C*R < K :
    print(0)
else :
    print(*find(C,R))