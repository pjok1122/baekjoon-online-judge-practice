'''
문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
입출력 예
number	k	return
1924	2	94
1231234	3	3234
4177252841	4	775841

[문제 풀이]

맨 앞 자리 수를 찾아나가는 방식으로 문제를 해결했다.

문제가 "4177252841", k=4 라고 해보자.

우리는 k=4이므로, 맨 앞자리 수가 '4','1','7','7','2' 중에 하나라는 사실을 알 수 있다.

즉, '4','1','7','7','2' 중에 가장 큰 수를 하나 선택하면 된다. 따라서 '7'을 선택하고 '7' 이전에 있는 숫자들은 모두 제거한다.

그럼 우리의 문제는 "7252841", k=2 라는 문제로 줄어들게 되므로 위와 같은 작업을 반복할 수 있다.

'''


def find_max(number):
    max_value = number[0]
    for num in number:
        if num > max_value:
            max_value = num
        if max_value == "9":
            break
    return max_value


def solution(number, k):
    answer = ''
    length = len(number)-k
    while k > 0 and len(answer) < length:
        leading_num = find_max(number[:k+1])
        answer += leading_num
        index = number.index(leading_num)
        k -= index
        number = number[index+1:]

    if len(answer) < length:
        answer += number

    return answer


print(solution("4177252841", 4))
print(solution("12", 1))
print(solution("999999999999999999", 17))
print(solution("1010", 2))
