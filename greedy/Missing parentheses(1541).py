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
