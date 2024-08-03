arr = [list(map(int,input().split())) for _ in range(5)]
input_list = []
for _ in range(5) :
    input_list += list(map(int,input().split()))

bingo = [[0] * 5 for _ in range(5)]
def check():
    global bingo
    bin = 0
    s1 = s2 = 0
    for i in range(5):
        s1 += bingo[i][i]
        s2 += bingo[4-i][i]
    if s1 == 5 :
        bin += 1
    if s2 == 5 :
        bin += 1
    
    for j in range(5):
        s3 = 0
        for i in range(5):
            s3 += bingo[i][j]
            if s3 == 5 :
                bin += 1

    for i in range(5):
        if sum(bingo[i]) == 5 :
            bin += 1

    if bin >= 3 : return True # 한번에 bingo개수가 4개가 될수도 있으니까 == 가 아닌 >= 임.
    else : return False

for inp in range(len(input_list)):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == input_list[inp] :
                bingo[i][j] = 1
                if check() == True : 
                    print(inp+1)
                    exit()