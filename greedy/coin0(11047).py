'''
    1. price[] 에 맞춰, 동전의 개수를 최소로 주는 문제.
    2. pirce는 오름차순으로 정렬되어있기 때문에 가장 비싼 동전부터 할당.
    3. 비싼 동전을 하나씩 주지 말고, 몇 개까지 한 번에 줄 수 있는지 결정한다.
    ex) 5200원을 500원 짜리와 100원을 최소로 주고 싶을 때, 500*10을 바로 할당하는 것이 보편적. 따라서 q = 5200/500 을 계산한다.
    4. 시간 복잡도 : O(n) 
'''

n, k = map(int, input().split())
price =[]
for i in range(n):
    price.append(int(input()))

idx=n-1
cnt=0
while idx>=0:
    if k==0:
        break
    if price[idx] > k :
        idx-=1
    else:
        q = k//price[idx]
        k-= price[idx]*q
        cnt+=q

print(cnt)
