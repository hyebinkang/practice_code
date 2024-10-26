
# 입력: 수열 a 크기, 수열 a
# 로직: 이분탐색, dp로도 가능, 리스트 하나 선언, 길어지는 것 찾기
# 리스트 숫자 확인, 들어오는 숫자 위치, 최종적으로 결과
# 긴 수열의 길이를 구하는것것# 출력: 가장 긴 증가하는 부분 수열 출력

import sys

N = int(sys.stdin.readline().strip())  # 수열 A 의 크기
A = list(map(int, sys.stdin.readline().strip().split()))  # 수열 A 에 대한 리스트 생성


def LIS(A):  # [10,20,30,40,50, 11,12,13,14,15,16,17]
    # LIS 저장할 리스트 ( 정확히는 LIS 는 아니지만, 일단 저 길이 를 위한)
    lis = []  # lis = []

    for a_num in A:  # lis = [10]  ->  [10,20,30,40,50]
        # 이진 탐색을 통해서, a_num 이 lis 에 들어갈 위치를 찾아 줄거에요
        left, right = 0, len(lis)
        while left < right:
            mid = (left + right) // 2  # mid =2    left = 0, right =5
            if lis[mid] < a_num:
                left = mid + 1
            else:
                right = mid  # right =2

        # left 가 a_num 이 들어갈 위치를 말해주는거
        if left == len(lis):  # lis = [10]  -> [10, 20]
            lis.append(a_num)  # 지금 A 라는 리스트에서 읽어온 새로운 숫자가 가장 클때
        else:
            lis[left] = a_num  # -> [10, 11, 20, 30, 40, 50]

    return len(lis)


print(LIS(A))

# [10,20,30,40,50,11,12,13,14,15,16,17]
