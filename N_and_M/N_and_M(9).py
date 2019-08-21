#순열, 중복을 포함하는 수열에서 중복되지 않는 순열을 출력.

def permutation(arr,cnt,result, depth,m):
    if(depth==m):
        print(' '.join(str(e) for e in result))
        return
    else:
        for i in range(len(cnt)):
            if cnt[i]:
                cnt[i]-=1
                result[depth] = arr[i]
                permutation(arr,cnt, result, depth+1,m)
                cnt[i]+=1


if __name__=="__main__":
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    result=[0]*m
    cnt = [1]
    loc=0
    i=1
    while(i<len(arr)):
        if (arr[i] ==arr[i-1]):
           cnt[loc]+=1
           arr.pop(i)
        else:
            i+=1
            loc+=1
            cnt.append(1)

    
    permutation(arr,cnt,result,0,m)
