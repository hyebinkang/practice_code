def solve(a):
    ans = 0
    for i in range(len(a)): #a의 개수
        ans += a[i] #a: list이기 때문에 a[i]
    return ans

solve([1,2,3,4,5])
