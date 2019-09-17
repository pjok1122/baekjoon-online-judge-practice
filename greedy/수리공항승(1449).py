N,L = map(int, input().split())

location = list(map(int,input().split()))
loaction.sort()

s = 0
e = 1
cnt=0
length = len(location)
while(True):
    if e>=length:
        e-=1
        cnt+=1
    if(L-1>=location[e]-location[s]):
        e+=1
        continue
    else:
        s=e-1
        cnt+=1
