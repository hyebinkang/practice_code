king, queen, rook, bishop, knight, pawn = map(int, input().split()) #입력받는 개수

print(1-king, 1-queen, 2-rook, 2-bishop, 2-knight, 8-pawn)      #올바른 세트 구성에 더 필요한 개수