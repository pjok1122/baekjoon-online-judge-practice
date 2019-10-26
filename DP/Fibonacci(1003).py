#피보나치 함수
'''
L[n]=[...] 공간에 f[n]을 호출 했을때 f(1)이 몇번, f(0)이 몇번 등장하는지 튜플로서 저장해둔다.
그리고 호출 될때마다 반복적으로 호출되는 연산을 막기 위해 L[n] R[n]이 존재할 경우에는 곧바로 참조한다.
'''

L=[-1 for x in range(41)]
R=[-1 for y in range(41)]

def FibCount(n):            #n번째 피보나치 수는 몇 번의 f(0)과 f(1)로 이루어져있는지 반환

    global L
    global R
    
    if L[n]!=-1:            #값이 저장되어 있다면 그 값을 반환
        return [L[n],R[n]]

    #베이스케이스 처리구간(인덱스오류 방지)
    if n==0:            
        L[0]=1
        R[0]=0
        return [L[0],R[0]]
    elif n==1:
        L[1]=0
        R[1]=1
        return [L[1],R[1]]
    
    else:                                       #캐시에 값을 저장하고 반환
        L[n]=FibCount(n-1)[0]+FibCount(n-2)[0]
        R[n]=FibCount(n-1)[1]+FibCount(n-2)[1]
        return [L[n],R[n]]


def main():
    T=int(input())
    for i in range(T):
        n= int(input())
        a,b=FibCount(n)
        print('%d %d' %(a,b))

if __name__=='__main__':
    main()
