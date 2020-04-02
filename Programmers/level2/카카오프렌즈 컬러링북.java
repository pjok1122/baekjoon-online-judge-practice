package algorithm;

import java.util.LinkedList;
import java.util.Queue;

public class Solution {
	
	static class Point{
		public int x;
		public int y;
		public int color;
		
		public Point(int x, int y, int color) {
			this.x = x;
			this.y = y;
			this.color = color;
		}
	}
	
	public static boolean checkIndex(int nx, int ny, int m, int n) {
		if(0 <= nx && nx<m && 0<=ny && ny<n) {
			return true;
		}
		else {
			return false;
		}
	}
	
	public static int[] solution(int m, int n, int[][] picture) {
	    Queue<Point> queue = new LinkedList<>();
		int[][] visited = new int[m][n];
		
		int numberOfArea = 0;
	    int maxSizeOfOneArea = 0;
	    int currentMaxSizeOfArea = 0;
		
		int[] dx = new int[] {1,-1,0,0};
		int[] dy = new int[] {0,0,1,-1}; 
		
		for(int i=0;i<m;i++) {
			for(int j=0;j<n;j++) {
				if(picture[i][j]!=0 && visited[i][j]==0) {
					numberOfArea++;
					visited[i][j] = 1;
					queue.add(new Point(i,j, picture[i][j]));
					currentMaxSizeOfArea = 0;
				}
				while(!queue.isEmpty()) {
					Point point = queue.poll();
					currentMaxSizeOfArea++;
					
					for(int k=0;k<4;k++) {
						int nx = point.x + dx[k];
						int ny = point.y + dy[k];
						
						if(checkIndex(nx, ny, m, n) && visited[nx][ny]==0 && picture[nx][ny] == point.color) {
							queue.add(new Point(nx,ny, picture[i][j]));
							visited[nx][ny]= 1;
						}
					}
				}
				if(currentMaxSizeOfArea > maxSizeOfOneArea) {
					maxSizeOfOneArea = currentMaxSizeOfArea;
				}
			}
		}
	    

	      
	    int[] answer = new int[2];
	    answer[0] = numberOfArea;
	    answer[1] = maxSizeOfOneArea;
	    return answer;
	}
	
	public static void main(String[] args) {
		int[][] picture = {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}};
		int[] solution = solution(6, 4, picture);
		System.out.println(solution[0]);
		System.out.println(solution[1]);
	}
}