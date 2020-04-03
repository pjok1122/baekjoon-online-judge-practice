def solution(n,a,b):
    count =0
    while(a!=b):
        count+=1
        a = a//2 if a%2==0 else a//2+1
        b = b//2 if b%2==0 else b//2+1

    return count

print(solution(8,4,7))