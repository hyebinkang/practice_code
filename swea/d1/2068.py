t = int(input())

for i in range(t):
    number = list(map(int, input().split()))                #입력받은 수를 리스트로 만들기

    print('#', i + 1, ' ',max(number), sep='')              #리스트의 최댓값 뽑기
