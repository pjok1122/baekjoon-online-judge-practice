string = input()
exploit = list(input())

stack = []
for char in string:  # 각 문자를 스택에 집어 넣는다.
    stack.append(char)
    # 스택에 들어있는 마지막 문자열이 폭발 문자열과 같다면 제거해준다.
    if stack[-len(exploit):] == exploit:
        for _ in range(len(exploit)):
            stack.pop(-1)

if stack:
    print(''.join(stack))
else:
    print('FRULA')
