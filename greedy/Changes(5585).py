'''
    1. 1000엔으로 물건을 산 후 거스름돈을 받는데, 동전이 최소가 되도록 하는 문제.
    2. 눈 여겨볼 점은 price[i] = k * price[i+1] , i>1로 설정되어있다는 점.
    3. 따라서 가장 비싼 동전부터 할당하는 것이 가능하다. 만약 배수가 아닌 경우, 거스름돈을 못 주는 경우가 발생할 수 있음.
    4. 이러한 경우에는 DP와 BFS를 이용할 수 있다. (최대 금액이 1000엔이기 때문.)
    5. 이 문제의 경우에는 단순히 비싼 동전부터 할당하면 되며, coin0 문제와 마찬가지로 해당 동전을 몇 개씩 거슬러 줄지 계산한다.
    6. 시간복잡도 : O(6) = O(1)
'''

n = int(input())
change = 1000 - n
price = [500,100,50,10,5,1]

idx=0
cnt=0
while idx<len(price):
    if change==0:
        break

    if price[idx] > change:
        idx+=1
    else:
        q = change // price[idx]
        change = change - price[idx]*q
        cnt+=q
        idx+=1

print(cnt)
