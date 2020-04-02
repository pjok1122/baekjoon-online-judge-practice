def solution(bishops):
    bs=[]
    for bishop in bishops:
        x = ord(bishop[0]) - ord('A')
        y = int(bishop[1]) - 1
        bs.append((x,y))
    
    visited =[[0 for col in range(8)] for row in range(8)]

    for bishop in bs:
        #왼쪽 대각선 위
        nx,ny = bishop
        visited[nx][ny]=1

        while(nx>0 and ny>0):
            nx -=1
            ny -=1
            visited[nx][ny] = 1
        
        #오른쪽 대각선 위
        nx,ny = bishop
        while(nx>0 and ny<7):
            nx -=1
            ny +=1
            visited[nx][ny] = 1

        #왼쪽 대각선 아래
        nx,ny = bishop
        while(nx<7 and ny>0):
            nx +=1
            ny -=1
            visited[nx][ny] = 1

        #오른쪽 대각선 아래
        nx,ny = bishop
        while(nx<7 and ny<7):
            nx +=1
            ny +=1
            visited[nx][ny] = 1 

    cnt=0
    for i in range(8):
        for j in range(8):
            if visited[i][j] == 0:
                cnt+=1               

    print(cnt)

solution(['D5'])
solution(["D5", "E8", "G2"])