def decimal_to_n(num, n):
    if(num==0):
        return '0'
    n_num = ''
    while(num!=0):
        n_num += str(hex(num%n)[2:]).upper()
        num = num//n
    n_num = n_num[::-1]
    return n_num

def solution(n, t, m, p):
    # n을 입력받았을 때, 각 숫자를 진법에 맞춰서 출력하는 것부터 시작.
    
    num = 0
    turn = 0
    my_turn = p-1
    answer = []

    #튜브가 미리 구할 숫자의 개수(t)를 다 찾을 때까지 반복.
    while t>0:
        # 각 숫자에 대해서 턴을 돌려본다.
        n_num = decimal_to_n(num, n)
        for d in n_num:
            # 다 찾았다면 스탑.
            if t<=0:
                break
            if turn%m == my_turn:
               answer.append(d)
               t = t-1
            turn+=1
        num+=1
    
    return ''.join(answer)
    
print(solution(2,4,2,1))
print(solution(16,16,2,1))