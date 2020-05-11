from collections import deque
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        if(image[sr][sc] == newColor):
            return image
            
        row_size = len(image)
        col_size = len(image[0])
        old_color = image[sr][sc]
        #큐에 초기값 할당.
        que = deque()
        image[sr][sc] = newColor
        que.append((sr,sc))

        dx = [1,-1, 0, 0]
        dy = [0, 0, 1,-1]
        while que:
            x, y = que.pop()

            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if 0<=nx<row_size and 0<=ny<col_size and image[nx][ny] == old_color:
                    image[nx][ny] = newColor
                    que.append((nx,ny))
                
        return image

sol = Solution()
print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1,1,2))
        