# 후위 표기법 계산, stack 사용
def cal(num):
    result = 0                                          # 결과를 저장할 변수
    stack = []                                          # stack
    for i in range(len(num)):                           # num의 길이만큼 반복, i번째가 숫자라면 스택에 저장
        if num[i].isdigit():
            stack.append(num[i])
        else:
            if result == 0:                             # result가 0 일 때 -> 처음 나온 연산자
                second = stack.pop()                    # 차례대로 한 개씩 빼줌
                first = stack.pop()

                if num[i] == '+':                       # 각 사칙연산 기호들에 맞게 계산
                    result = int(first)+int(second)
                elif num[i] == '-':
                    result = int(first)-int(second)
                elif num[i] == '*':
                    result = int(first)*int(second)
                else:
                    result = int(first)//int(second)
            else:                                       # result가 0 이 아닐 때 -> 두번째 이상 나온 연산자
                third = stack.pop()

                if num[i] == '+':                       # 사칙연산 기호들에 맞게 계산
                    result += int(third)
                elif num[i] == '-':
                    result -= int(third)
                elif num[i] == '*':
                    result *= int(third)
                else:
                    result //=int(third)

    return result

print(cal(list(input().split())))


# 더 간단히 하는 코드 -> GPT한테 도움 받았습니다..
def cal(num):
    stack = []
    for i in num:
        if i.isdigit():                         # 숫자일 경우 스택에 추가
            stack.append(int(i))
        else:                                   # 연산자일 경우
            second = stack.pop()                # 스택에서 두 개의 숫자를 꺼냄
            first = stack.pop()

            if i == '+':                        # 계산 한 결과를 스택에 저장
                stack.append(first + second)    # -> 스택에 쌓인 숫자가 두개라서 first, second를 활용할 수 있음
            elif i == '-':
                stack.append(first - second)
            elif i == '*':
                stack.append(first * second)
            elif i == '/':
                stack.append(first // second)

    return stack.pop()                      # 최종 결과 반환

print(cal(input().split()))
