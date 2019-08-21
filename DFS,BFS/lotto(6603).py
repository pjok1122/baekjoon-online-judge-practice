# from itertools import combinations

def Combination(S, depth, result, index):
    if depth==6:
        print(' '.join(map(str, result)))
        return
    else:
        for i in range(index, len(S)):
            result[depth] = S[i]
            Combination(S, depth+1, result, i+1)

while True:
    _tmp = list(map(int, input().split()))
    k = _tmp[0]
    S = _tmp[1:]
    result = [0]*6

    if k==0:
        break
    Combination(S,0,result,0)
    print()