#-----------리스트일 때
def solve(a):
    ans = 0
    for i in range(len(a)): #a의 개수
        ans += a[i] #a: list이기 때문에 a[i]
    return ans

solve([1,2,3,4,5])
#-----------정수일 때
def solve1(a):
    ans = 0
    for i in range(a+1): #a의 개수
        ans += i #a: list이기 때문에 a[i]
    return ans

print(solve1(5))