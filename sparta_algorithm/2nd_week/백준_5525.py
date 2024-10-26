N = int(input())        # P_N 결정하는 N의 수
S = int(input())             # 문자열의 길이)
L = input()             # I, O로 이루어져 있는 문자열

P = 'IOI' + 'OI' * (N-1)
result = 0

for i in range(S):
    if L[i] == 'O':
        continue
    if L[i] == 'I':
        if L[i:i+len(P)] == P:
            result +=1

print(result)