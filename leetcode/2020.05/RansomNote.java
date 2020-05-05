package leetcode.2020.05;

public class RansomNote {
    class Solution {
        public boolean canConstruct(String ransomNote, String magazine) {
            int[] lower = new int[26];
            for(int i=0; i<magazine.length();i++){
                char c = magazine.charAt(i);
                lower[c-'a'] +=1;
            }
            
            for(int i=0; i<ransomNote.length();i++){
                char c = ransomNote.charAt(i);

                if(lower[c-'a'] > 0){
                    lower[c-'a']-=1;
                } else{
                    return false;
                }
            }

            return true;
        }
    }
}