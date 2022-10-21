#주사위를 굴려 같은 눈이 눈에 따라 상금을 받게 되는 코드 작성
dice = list(map(int, input().split()))  #주사위 3개 수를 리스트로 받음
set_dice = list(set(dice))              #dice에서 중복된 숫자를 제거한 리스트를 만듬

if (len(set_dice) == 3):                #3개 모두 다른 수 일 때
    print(max(dice) * 100)
elif(len(set_dice) == 2):               #2개가 같은 수 일 때
    for i in range(2):                  #for문을 사용 하여 set_dice 와 dice비교
        if(set_dice[i] in dice):        #set_dice에 있는 수를 dice와 비교
            dice.remove(set_dice[i])    #dice의 수를 지우면 중복된 하나의 수가 남게 됨 = 중복되는 수
            print(dice)
    print(1000 + dice[0]*100)           #남은 하나의 수를 이용하여 계산
else:
    print(10000+set_dice[0]*1000)       #3개가 모두 같은 수 일 때 (len(set_dice) == 1)