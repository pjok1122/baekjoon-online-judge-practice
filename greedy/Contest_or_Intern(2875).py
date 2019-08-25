N,M,K = map(int,input().split())

max = 0
while True:
    N-=2
    M-=1
    if N<0 or M<0 or (N+M)< K:
        break
    max+=1
print(max)