
public class ReverseString {
    
	public static void reverseString(char[] s) {
	    char printVal = 0;
	    for(int i=0;i<s.length;i++){
	        if(s[i]!=0){
	            printVal = s[i];
	            s[i] = 0;
	            reverseString(s);
	            s[s.length-i-1] = printVal;
	            break;
	        }
	    }
    }
	
	public static void main(String[] args) {
		char s[] = new char [] {'h','e','l','l','o'};
		reverseString(s);
		for(int i=0;i<s.length;i++) {
			System.out.print(s[i]+" ");
		}
	}
}
