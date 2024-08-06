def check(sq1_x1,sq1_y1,sq1_x2,sq1_y2,sq2_x1,sq2_y1,sq2_x2,sq2_y2) :
    if sq1_x2 < sq2_x1 or sq1_x1 > sq2_x2 or sq1_y2 < sq2_y1 or sq1_y1 > sq2_y2:
        return 'd'  # 겹치지 않음

    if (sq1_x2 == sq2_x1 or sq1_x1 == sq2_x2) and (sq1_y2 == sq2_y1 or sq1_y1 == sq2_y2):
        return 'c'  # 점에서 겹침

    if (sq1_x2 == sq2_x1 or sq1_x1 == sq2_x2) or (sq1_y2 == sq2_y1 or sq1_y1 == sq2_y2):
        return 'b'  # 선분에서 겹침

    return 'a'  # 면에서 겹침

for _ in range(4) :
    sq1_x1,sq1_y1,sq1_x2,sq1_y2,sq2_x1,sq2_y1,sq2_x2,sq2_y2 = map(int,input().split())
    print(check(sq1_x1,sq1_y1,sq1_x2,sq1_y2,sq2_x1,sq2_y1,sq2_x2,sq2_y2))