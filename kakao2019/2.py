def rightString(p):
    if len(p)==0:
        return 0

    for _ in range(len(p)):
        p_comp = p
        p = p.replace("()", "")
        if len(p) == len(p_comp):
            return 0
        elif len(p) == 0:
            return 1

def solution(p):
    u,v ='',''
    cnt1=0
    cnt2=0
    if len(p)==0:
        return ''

    for i in range(len(p)):
        if p[i] =='(':
            cnt1 += 1
            u += '('
        else:
            cnt2 += 1
            u += ')'
        
        if cnt1 == cnt2:
            v = p[i+1:]
            break
    
    if rightString(u):
        u += solution(v)
        return u
    else:
        tmp = '('
        tmp += solution(v)
        tmp += ')'

        for i in range(1,len(u)-1):
            if u[i]=='(':
                tmp+=')'
            else:
                tmp+='('
        
        return tmp

# print(solution("(()())()"))
# print(solution(")("))
# print(solution("()))((()"))
print(solution("))()(("))