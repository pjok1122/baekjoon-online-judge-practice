'''
 1. B의 부분 문자열 중에서 A 문자열과 가장 일치하는 부분을 찾는다.
 2. A의 문자열의 앞 뒤에 B의 문자열과 일치하도록 삽입한다. (문제 풀이에 필요 없음.)
 3. 시간 복잡도 : O(25*25/4)= O(1), 사이즈가 너무 작음.
'''

a,b = input().split()

index = len(b)-len(a)+1

Min = 50
for i in range(index):
    diff=0
    for j in range(len(a)):
        if a[j]!=b[i+j]:
            diff+=1

    if diff<Min:
        Min = diff

print(Min)
