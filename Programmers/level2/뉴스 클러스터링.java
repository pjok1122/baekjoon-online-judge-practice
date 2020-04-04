package javaproject;

import java.util.HashMap;
import java.util.Map;

public class Main {
	
	public static boolean isAlphabet(char ch) {
		if('a' <= ch && ch<='z') {
			return true;
		}
		return false;
	}
	
	public static void stringToMap(String str, Map<String, Integer> map) {
		for(int i=0;i<str.length()-1;i++) {
			String subString = str.substring(i, i+2);
			if(isAlphabet(subString.charAt(0)) && isAlphabet(subString.charAt(1))) {
				if(!map.containsKey(subString)) {
					map.put(subString, 1);
				} else {
					map.put(subString, map.get(subString) + 1);
				}
			}
		}
	}
	
	public static int solution(String str1, String str2) {
		Map<String, Integer> map = new HashMap<String,Integer>();
		Map<String, Integer> map2 = new HashMap<String,Integer>();
		
		stringToMap(str1.toLowerCase(), map);
		stringToMap(str2.toLowerCase(), map2);
		
		int common = 0;
		int sum = 0;

		for(String str : map.keySet()) {
			if(!map2.containsKey(str)) {
				sum += map.get(str);
				continue;
			} else {
				common += Math.min(map.get(str), map2.get(str));
				sum += Math.max(map.get(str), map2.get(str));
			}
		}
		
		for(String str : map2.keySet()) {
			if(!map.containsKey(str)) {
				sum += map2.get(str);
			}
		}
		
		double jaccard = sum > 0 ? common/(double)sum : 1;
		int answer = (int)(jaccard * 65536);
		
		return answer;
	}
	
	public static void main(String[] args) {
//		System.out.println(solution("FRANCE", "french"));
		System.out.println(solution("aa1+aa2", "AAAA12"));
	}
}
