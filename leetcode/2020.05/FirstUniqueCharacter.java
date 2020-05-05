package leetcode.2020.05;

public class FirstUniqueCharacter {
    class Solution {
        public int firstUniqChar(String s) {
            int[] count = new int[26];
            for(int i=0;i<s.length();i++){
                count[s.charAt(i)-'a'] +=1;
            }
            
            for(int i=0;i<s.length();i++){
                if(count[s.charAt(i)] == 1){
                    return i;
                }
            }
            
            return -1;
        }
    }
}