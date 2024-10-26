# 중복 문자 없는 가장 긴 부분 문자열, 해시테이블
def letter(eng):
    hash = {}                               # 해시테이블 -> 딕셔너리 저장
    num = 0                                 # 딕셔너리의 key값
    for i in range(len(eng)):
        if len(hash) == 0:                  # 아무것도 없으면 첫번째 값을 딕셔너리로 저장
            hash[i] = eng[i]
        else:
            if eng[i] not in hash[num]:     # 가장 마지막에 입력된 딕셔너리에 중복되지 않는 것이 있다면
                hash[num] += eng[i]         # 문자열로 이어 붙임
            else:
                num +=1                     # 중복되는 것이 있다면, 새로운 key값으로 값을 저장
                hash[num] = eng[i]

    result = 0                             # value의 길이 비교
    for i in hash.values():
        if len(i) > result:
            result = len(i)

    return result


print(letter(input()))

# GPT 한테 물어본 코드
def letter(eng):
    hash_set = set()  # 중복 문자를 확인하기 위한 해시셋
    left = 0  # 윈도우의 왼쪽 끝
    max_len = 0  # 중복이 없는 가장 긴 문자열의 길이

    for right in range(len(eng)):  # 오른쪽 포인터로 문자열을 순회
        # 중복된 문자가 있으면 왼쪽 포인터를 옮기며 중복 제거
        while eng[right] in hash_set:
            hash_set.remove(eng[left])
            left += 1
        # 중복이 없다면 문자 추가
        hash_set.add(eng[right])
        # 최대 길이 갱신
        max_len = max(max_len, right - left + 1)

    return max_len


print(letter(input()))
