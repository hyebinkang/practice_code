n = int(input())

three_cnt = 0   #3kg봉지 cnt

five_cnt = 0    #5kg봉지 cnt
five_cnt_re = 0 #5kg봉지 cnt의 나머지

best = []   #5kg + 3kg 가능한 경우의 리스트

for i in range(n):  #n번 만큼 for문 실행

    three_cnt = i   #0부터 대입

    five_cnt = (n - 3 * three_cnt) // 5 #5cnt 구하는 공식 (몫)
    five_cnt_re = (n - 3 * three_cnt) % 5   #5cnt 나머지 공식
    if five_cnt_re == 0 and five_cnt >= 0:  #5cnt의 나머지가 0이고. 몫이 0과 같거나 클 경우
        best.append(three_cnt + five_cnt)   #3kg +5kg
    elif five_cnt < 0:  #음수의 경우 break
        break

if best == []:  #리스트안에 아무것도 없으면
    print(-1)

else:
    print(min(best))    #있을 때 최솟값 출력

