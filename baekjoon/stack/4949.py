while True:
    small = []                      #스택

    sentence = input()
    if sentence == '.':             #.이 오면 종료
        break

    for spell in sentence:
        if spell == '(':
            small.append(spell)
        elif spell == ')':
            if len(small) !=0:              #스택 길이가 0이 아니어야 실행
                if small[-1] == '(':        #가장 상위의 것과 같은지 확인
                    small.pop()
                else:
                    small.append(spell)     #아니라면 spell넣기
            else:
                small.append(spell)
                break
        elif spell =='[':
            small.append(spell)
        elif spell ==']':
            if len(small) !=0:
                if small[-1] == '[':
                    small.pop()
                else:
                    small.append(spell)
            else:
                small.append(spell)
                break
        else:
            continue

    if not small:       #스택이 전부 비었음 = 균형잡힌 문장
        print('yes')
    else:
        print('no')