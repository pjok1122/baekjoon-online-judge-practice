'''
[문제 설명]

124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

124 나라에는 자연수만 존재합니다.
124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

10진법	124 나라	10진법	124 나라
1	1	6	14
2	2	7	21
3	4	8	22
4	11	9	24
5	12	10	41
자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.

제한사항
n은 500,000,000이하의 자연수 입니다.
입출력 예
n	result
1	1
2	2
3	4
4	11

[문제 풀이]

생각보다 제법 어려운 문제다. 수학적인 직관과 컴퓨팅적인 사고 모두를 요하고 있다.

수학적인 직관은 그다지 어렵지 않다. "숫자 3개로 표현하는 것이니, 3진법을 이용하자!" 라는 사실이다.

즉 124 나라의 1은 0에 대응되고 2는 1에 대응되고 4는 2에 대응되도록 한다는 것이다.

하지만 이 논리에는 당연히 문제가 발생한다.

애초에 10진법의 1이 124나라의 1에 대응되므로 3진법을 적용하기 위해서는 10진법의 숫자에서 1을 빼주어야 매칭이 된다는 사실이다.

그럼 다른 부분에서는 문제가 발생하지 않을까? 마찬가지로 문제가 발생한다.

여기서 "수의 관점"으로 접근한다면 굉장히 복잡해진다. 124나라가 숫자 "1"과 "0"을 혼용해서 사용하고 있기 때문에 어떻게 이를 조정해줘야 할지 갈피를 잡기가 힘들다.

물론, 가능하다.

하지만, 더 쉬운 관점이 있다.

바로 프로그래밍적 관점이다.

n을 3진법으로 나타내면 다음과 같은 형태로 나타날 것이다.

n = an ... a1 a0

여기서 a0을 제외하고는 전부 3의 배수이므로 n%3을 하면 a0의 값을 구할 수 있다.

하지만, 위에서 봤듯, 124나라의 숫자를 반영하려면 n에서 1을 빼주고 3진법으로 나타내야 한다.

따라서 a0 = "124"[(n-1)%3] 라는 사실을 알 수 있다.

a1을 구하는 방법도 그다지 어렵지 않다. (n-1)의 값을 3으로 나누어주면, a1을 제외하고는 모두 3의 배수가 된다.

따라서 위와 똑같은 방식으로 a1부터 an까지 찾아나갈 수 있다.





'''


def solution(n):
    answer = ''
    while(n > 0):
        n -= 1
        answer += "124"[n % 3]
        n //= 3
    return answer[::-1]
