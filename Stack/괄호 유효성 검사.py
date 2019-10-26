# () ,{}, [] 추가 되어도 같은 방식으로 구현가능.
# left = ['(', '{', '[']
# right = [')', '}', ']']


def check_parentheses(datas):
    stack = []

    for data in datas:
        if data == '(':
            stack.append(data)
        elif data == ')':
            if len(stack) > 0:
                stack.pop(-1)
            else:
                return 0

    if len(stack) == 0:
        return 1
    else:
        return 0


print(check_parentheses("()((abc))"))
