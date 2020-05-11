package leetcode.2020.05;

public class CheckStraightLine {
    class Solution {
        public boolean checkStraightLine(int[][] coordinates) {
            double dd = (coordinates[1][1] - coordinates[0][1])/(double)(coordinates[1][0] - coordinates[0][0]);
            for(int i=2;i<coordinates.length;i++) {
                if(dd != (coordinates[i][1] - coordinates[i-1][1])/(double)(coordinates[i][0] - coordinates[i-1][0])){
                    return false;
                }
            }
            return true;
        }
    }
}