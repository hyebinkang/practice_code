N = int(input())

num_list = list(sorted(map(int, input().split())))  #중앙값: 원소들을 크기 순으로 배열한 후 가장 가운데에 있는 값

mid = N//2                                          #홀수의 N값만을 사용함

print(num_list[mid])                                #mid번째에 있는 중앙값 출력
