x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))      #직사각형 w,h까지 도달하기 위한 최솟값 구하기