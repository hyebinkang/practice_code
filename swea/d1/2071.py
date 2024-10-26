num = int(input())

for i in range(num):
    test_list = list(map(int, input().split()))     #입력받은 수를 리스트로 만들기
    print('#',i+1,' ',round(sum(test_list)/10), sep='')     #리스트를 사용하여 평균값 구하기