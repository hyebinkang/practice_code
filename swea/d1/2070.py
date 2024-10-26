t = int(input())

for i in range(t):
    first, second = map(int, input().split())       #두 수를 입력 받아서 비교하기

    if first > second:
        print('#',i+1,' ','>', sep='')
    elif first == second:
        print('#',i+1,' ','=', sep='')
    else:
        print('#', i+1, ' ', '<', sep='')