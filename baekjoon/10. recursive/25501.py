def recursion(s, l, r):
    global count                            #count를 전역변수로 이용
    count +=1                               #횟수 +1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):                        #팰린드롬 여부 확인
    return recursion(s, 0, len(s)-1)

t = int(input())
for i in range(t):
    s = input()
    count = 0
    print(isPalindrome(s), count)
