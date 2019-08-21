#데이터가 주어져있을 때, 조합

def combination(arr, visited, start, n, r):
    if(r==0):
        PrintArray(arr, visited, n)
        return
    for i in range(start, n):
        visited[i] = 1
        combination(arr, visited, i+1, n, r-1)
        visited[i] = 0
    return
    
def PrintArray(arr, visited, n):
    result =''
    for i in range(n):
        if(visited[i]):
            result+=str(arr[i])+' '
    print(result)
    
if __name__=="__main__":
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    visited = [0]*n
    combination(arr,visited, 0, n, m)
