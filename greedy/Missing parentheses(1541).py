'''
[문제 풀기 전 생각할 것]

수식이 나열되어있을 때, 괄호를 어디에 쳐야하는 지를 파악한다.

1+2-3+4+5+6-7+8+9 라는 수열이 주어지면, 괄호는 다음과 같이 쳐야 한다.

1+2-(3+4+5+6)-(7+8+9)

즉, -부호일 때 괄호를 열고 다시 -부호를 만날 때 괄호를 닫아준다.

물론, 끝까지 -부호를 안만날 수도 있기 때문에 수의 끝에 도달해도 괄호를 닫는다.

논리는 비교적 쉬우나, 구현할 때는 조금 짜증나는 문제가 될 수 있다.
'''

data='+'
data += input()
length = len(data)
i=0
filtered_data=''
while i< length:
    if data[i]=='+' or data[i]=='-':
        filtered_data +=data[i]
        i+=1
        while i<length and data[i]=='0':
            i+=1
    filtered_data +=data[i]
    i+=1
#print(filtered_data)

i=1
open=1
close=0
result_str=''
while i<len(filtered_data):
    if filtered_data[i]=='-' and open:
        result_str +='-('
        open,close = 0,1
    elif filtered_data[i]=='-' and close:
        result_str +=')-('
    else:
        result_str += filtered_data[i]
    i+=1

if close:
    result_str+=')'

#print(result_str)
print(eval(result_str))
