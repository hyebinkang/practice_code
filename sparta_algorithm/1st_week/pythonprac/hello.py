# people = [{'name': 'bob', 'age': 20},
#           {'name': 'carry', 'age': 38},
#           {'name': 'john', 'age': 7},
#           {'name': 'smith', 'age': 17},
#           {'name': 'ben', 'age': 27}]
#
# class Person:
#     def __init__(self, name):       # self:나
#         self.name = name
#
#     def sayhello(self, toWhom):
#         print(f"hello,{toWhom}. I am {self.name}")
#
# rtan = Person("르탄")
# rtan.sayhello("에이블")
# import requests # requests 라이브러리 설치 필요
#
# r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
# rjson = r.json()
#
# gus = rjson['RealtimeCityAir']['row']
#
# for gu in gus:
# 	print(gu['MSRSTE_NM'], gu['IDEX_MVL'])

## 알파벳 찾기
import string


def get_idx_naive(word):
		# O(N^2)
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        char = word[i]
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:
                result[j] = i
    return result


def get_idx(word):
    # O(N)
    result = [-1]*len(string.ascii_lowercase)		# ascii_letters-> 모든 문자
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        if result[idx] == -1:
            result[idx] = i
    return result


print(get_idx_naive('sparta'))
print(get_idx('sparta'))

import string

# 1. 알파벳을 바로 꺼내오는 방법
print(string.ascii_lowercase)

# 2. ord 연산
print(ord('a'), ord('A'), ord('@'))  # 97 65 64

# 3. range
for i in range(10):
    print(i)