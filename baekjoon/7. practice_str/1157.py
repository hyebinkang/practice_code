new_word = input().upper()          #입력받은 문자를 대문자로 하기

set_word = list(set(new_word))      #중복되는 알파벳은 하나의 값으로 남기기
cnt = []                            #개수 세기 리스트

for i in set_word:                  #중복 제거된 set_word안에서 for문 실행
    cnt.append(new_word.count(i))   #cnt에 new_word에서 받은 문자의 알파벳 개수를 세서 append

if cnt.count(max(cnt)) > 1:         #cnt에 저장된 개수 중 최고값이 1개를 초과하면
    print('?')                      #출력
else:                               #1개를 초과 하지 않을 경우
    print(set_word[cnt.index(max(cnt))])    #최댓값의 인덱스 값을 set_word의 인덱스 값으로 이용




# 단어의 길이가 1,000,000까지 가능하기때문에
#
# 길이가 최대(n)인 for문 내부에서 count함수를 사용하면
#
# 시간복잡도가 O(n^2)가 되어 시간초과가 날 수도 있습니다.
#
# import sys                            #시간 초과로 읽기 속도를 빠르게 하기 위해 사용
# word = sys.stdin.readline()           #문자 입력받기
# up_word = word.upper()                #입력받은 문자를 대문자로
# alphabet = []                         #각 문자를 리스트 안의 원소로 저장
# cnt = []                              #alphabet의 사용 횟수를 저장하기 위한 리스트
#
# for i in up_word:
#     alphabet.append(i)                #입력 받은 단어를 한 글자마다 리스트 원소로 저장
#     cnt.append(alphabet.count(i))     #알파벳 안에서 문자 i의 횟수를 cnt에 저장
#
# if cnt.count(max(cnt)) > 1:           #cnt에서 가장 큰 값이 1개 초과이면
#     print('?')                        #출력
# else:                                 #1개인 경우
#     print(alphabet[cnt.index(max(cnt))])    #cnt의 최댓값의 인덱스값을 알파벳의 인덱스로 가져와서 문자 출력