'''
주어진 수를 적절히 묶어, 최댓값을 갖게 하는 문제.

[문제 풀기 전에 생각해야 할 것]

어떻게 묶어야 값이 커지는 지를 파악해야 한다.

예를 들어, [-3,-2, 0,1,2,3] 이라는 숫자가 있다면,
(-3)*(-2), 0, 1, (2*3) 으로 만들고 더 해주면 가장 큰 값인 13을 갖는다.

이 논리를 정리하면, 다음과 같다.

1) 음수는 작은 수 끼리 묶는다.
2) 양수는 큰 수 끼리 묶는다.
3) 0은 더하나 마나 제외.

[알고리즘]

안타깝게도 위 논리에는 예외가 있다. 따라서 좀 더 명쾌하게 정리하는 작업이 필요하다.

예를 들어, [1,1,1,1] 이라는 숫자가 있다면 어떨까? 위에 정의한 알고리즘을 사용하면 (1*1)+(1*1)=2
라는 결과를 얻게 된다. 하지만, 이 경우에는 4가 정답이 된다.

따라서, 위 논리를 조금 수정하면,

1) 음수는 작은 수 끼리 묶는다.
2) 숫자가 1인 경우 묶지 않는다. 
3) 양수는 큰 수 끼리 묶는다.
4) 0은 제외한다.

안타깝게도 이 논리도 예외가 발생한다. 이 모든 과정은 필자가 직접 경험했던 루틴이다..

예를 들어, [-1,0] 이라는 숫자가 있다면 어떨까? 위에 정의한 알고리즘 대로라면 -1을 반환한다.
하지만, (-1)*0 = 0이므로 0이 정답이 된다. 즉, 0은 음수 쪽에 같이 묶어주는 것으로 해결 가능하다.

[최종 알고리즘]

1) 0을 포함한 음수는 작은 수 부터 묶는다.
3) 1보다 큰 수는 큰 수부터 묶는다.
2) 숫자가 1인 경우에는 묶지 않는다.

편의상, negative와 positive라는 리스트 정의해서 1), 2)를 정렬하여 사용한다. 

'''


import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

negative=[]
positive=[]
ans=0
for num in nums:
    if num<=0:      #0도 negative의 원소로 둔다.
        negative.append(num)
    elif num==1:
        ans+=1      #숫자가 1인 경우에는 묶지 않으므로, 미리 계산하여 둔다.
    elif num>1:
        positive.append(num)

# 목적에 맞게 정렬
negative.sort()
positive.sort(reverse=True)

# 1) 작은 수부터 차례대로 묶는다.
for i in range(0,len(negative),2):
    if i+1 < len(negative):
        ans += negative[i]*negative[i+1]
    else:
        ans += negative[i]

# 2) 큰 수부터 차례대로 묶는다.
for i in range(0,len(positive),2):
    if i+1 < len(positive):
        ans += positive[i]*positive[i+1]
    else:
        ans += positive[i]

print(ans)