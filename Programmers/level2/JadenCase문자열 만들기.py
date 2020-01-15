'''
[문제 설명]

JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
s는 길이 1 이상인 문자열입니다.
s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )
입출력 예
s	return
3people unFollowed me	3people Unfollowed Me
for the last week	For The Last Week

[문제 풀이]

쉬운 문제. 띄어쓰기가 2개 이상일 수 있으므로 split()을 이용해서 풀 수 없다.

우선 띄어쓰기를 만났을 때마다 다음 문자를 대문자로 바꿔주면 된다.

하지만 이렇게 생각하는 것보다, 각 문자마다 이전 문자가 띄어쓰기 였는지 판단하는 것이 좋다.

인덱스 관리도 편하고, 이전문자가 띄어쓰기 였는가 아닌가 두 개로 편하게 구분이 가능하다.

'''


# def solution(s):
#     return s.title()


def solution(string):
    answer = string[0].upper()
    i = 1
    while(i < len(string)):
        if string[i-1] == " ":
            answer += string[i].upper()
            i += 1
        else:
            answer += string[i].lower()
            i += 1

    return answer


print(solution("3people unFollowed me"))
print(solution("ab bc 3c 4dvf"))
print(solution("  "))
print(solution("ab  bc"))
