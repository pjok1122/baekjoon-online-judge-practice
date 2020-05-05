public class JwelsAndStones {
    class Solution {
        public int numJewelsInStones(String J, String S) {
            int[] upper = new int[26];
            int[] lower = new int[26];
            int result =0;
            for(int i=0; i<S.length();i++){
                char c = S.charAt(i);
                if('a'<= c && c<='z'){
                    lower[c-'a'] +=1;
                } else{
                    upper[c-'A'] +=1;
                }
            }
            
            for(int i=0;i<J.length();i++){
                char c = J.charAt(i);
                if('a'<=c && c<='z'){
                    result += lower[c-'a'];
                } else{
                    result += upper[c-'A'];
                }
            }
            
            return result;
        }
    }   
}