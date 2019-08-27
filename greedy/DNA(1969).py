'''
주어진 DNA 문자열에서 Hamming Distance의 합이 최소가 되도록 하는 문제.
1. 가장 많이 등장하는 뉴클레오티드('문자')를 세고 그 값을 Max로 설정. 가장 많이 등장하는 문자가 H.D가 최소가 되도록 하므로 DNA 결과(result)에 포함시킨다.
2. 하나의 뉴클레오티드가 결정될 때마다 H.D의 값은 N - Max 만큼 증가한다.
3. 시간복잡도 : O(N*M) ~ O(N)
'''
N,M = map(int,input().split())
dna = []
result =''
hd = 0
for i in range(N):
    dna.append(input())

for i in range(M):
    cnt = [0,0,0,0]
    for j in range(N):
        if dna[j][i] == 'A':
            cnt[0] +=1
        elif dna[j][i] =='C':
            cnt[1] +=1
        elif dna[j][i] == 'G':
            cnt[2] +=1
        elif dna[j][i] == 'T':
            cnt[3] +=1

    Max = max(cnt)
    idx = cnt.index(Max)
    if idx ==0:
        result+='A'
    elif idx==1:
        result+='C'
    elif idx==2:
        result+='G'
    elif idx==3:
        result+='T'
    hd += N - Max

print(result)
print(hd)