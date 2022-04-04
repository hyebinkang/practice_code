def isPrime(num):
    if num == 1:
        return False
    elif num !=1:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        array.append(num)
        return True           #소수인 것들에 True반환
    # elif num == True:
    #
    #     return num



while True:
    M = int(input())
    array = []
    if M == 0:
        break

    for i in range(M+1, M*2+1):
        isPrime(i)
        print(len(array))
        break




