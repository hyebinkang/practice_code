n = int(input())

three_cnt = 0

five_cnt = 0
five_cnt_re = 0

best = []

for i in range(n):

    three_cnt = i

    five_cnt = (n - 3 * three_cnt) // 5
    five_cnt_re = (n - 3 * three_cnt) % 5
    if five_cnt_re == 0 and five_cnt >= 0:
        best.append(three_cnt + five_cnt)
    elif five_cnt < 0:
        break

if best == []:
    print(-1)

else:
    print(min(best))

