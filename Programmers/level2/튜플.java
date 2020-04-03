/**
 * [문제 설명]
	셀수있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음을 튜플(tuple)이라고 합니다. n개의 요소를 가진 튜플을 n-튜플(n-tuple)이라고 하며, 다음과 같이 표현할 수 있습니다.
	
	(a1, a2, a3, ..., an)
	튜플은 다음과 같은 성질을 가지고 있습니다.
	
	중복된 원소가 있을 수 있습니다. ex : (2, 3, 1, 2)
	원소에 정해진 순서가 있으며, 원소의 순서가 다르면 서로 다른 튜플입니다. ex : (1, 2, 3) ≠ (1, 3, 2)
	튜플의 원소 개수는 유한합니다.
	원소의 개수가 n개이고, 중복되는 원소가 없는 튜플 (a1, a2, a3, ..., an)이 주어질 때(단, a1, a2, ..., an은 자연수), 이는 다음과 같이 집합 기호 '{', '}'를 이용해 표현할 수 있습니다.
	
	{{a1}, {a1, a2}, {a1, a2, a3}, {a1, a2, a3, a4}, ... {a1, a2, a3, a4, ..., an}}
	예를 들어 튜플이 (2, 1, 3, 4)인 경우 이는
	
	{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
	와 같이 표현할 수 있습니다. 이때, 집합은 원소의 순서가 바뀌어도 상관없으므로
	
	{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
	{{2, 1, 3, 4}, {2}, {2, 1, 3}, {2, 1}}
	{{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}}
	는 모두 같은 튜플 (2, 1, 3, 4)를 나타냅니다.
	
	특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.
	
	[제한사항]
	s의 길이는 5 이상 1,000,000 이하입니다.
	s는 숫자와 '{', '}', ',' 로만 이루어져 있습니다.
	숫자가 0으로 시작하는 경우는 없습니다.
	s는 항상 중복되는 원소가 없는 튜플을 올바르게 표현하고 있습니다.
	s가 표현하는 튜플의 원소는 1 이상 100,000 이하인 자연수입니다.
	return 하는 배열의 길이가 1 이상 500 이하인 경우만 입력으로 주어집니다.
	[입출력 예]
	s	result
	"{{2},{2,1},{2,1,3},{2,1,3,4}}"	[2, 1, 3, 4]
	"{{1,2,3},{2,1},{1,2,4,3},{2}}"	[2, 1, 3, 4]
	"{{20,111},{111}}"	[111, 20]
	"{{123}}"	[123]
	"{{4,2,3},{3},{2,3,4,1},{2,3}}"	[3, 2, 4, 1]
	입출력 예에 대한 설명
	입출력 예 #1
	문제 예시와 같습니다.
	
	입출력 예 #2
	문제 예시와 같습니다.
	
	입출력 예 #3
	(111, 20)을 집합 기호를 이용해 표현하면 {{111}, {111,20}}이 되며, 이는 {{20,111},{111}}과 같습니다.
	
	입출력 예 #4
	(123)을 집합 기호를 이용해 표현하면 {{123}} 입니다.
	
	입출력 예 #5
	(3, 2, 4, 1)을 집합 기호를 이용해 표현하면 {{3},{3,2},{3,2,4},{3,2,4,1}}이 되며, 이는 {{4,2,3},{3},{2,3,4,1},{2,3}}과 같습니다.
 * 
 *  [문제 풀이]
 *  
 *  문제에 대한 아이디어를 떠올리는 것은 그다지 어렵지 않다.
 *  
 *  가장 작은 배열 {2} 이 시작이 되고, 그 다음 배열이 {2,3}이라면 다음 숫자는 3이 된다.
 *  따라서 우리는 문자열을 적절히 정리할 수 있어야 한다.
 *  
 *  split을 적절히 사용해서 데이터를 정리하고, HashMap을 사용해서 데이터의 개수별로 할당했다.
 *  
 *  예를 들자면 이렇다.
 *  hashMap[1] = {2}
 *  hashMap[2] = {2,3}
 *  hashMap[3] = {3,2,4}
 *  hashMap[4] = {3,2,4,1}
 *  
 *  최종 배열의 길이는 500이므로 answer[i]를 찾는 과정은 최대 500번만 일어난다.
 *  
 *  answer[i]를 찾는 과정은 hashMap[i]에서 hashMap[i-1]에 들어있지 않은 숫자를 찾으면 되므로, 시간복잡도는 최대 O(n^2)이다.
 *  
 *  최종 시간복잡도는 O(n^3)이지만 여기서 n의 최댓값은 500이므로 500*500*500이 최대이다. 이 값은 125000000 == 2^20 정도로 다항시간 내에 충분히 계산이 가능하다.
 *  
 *  
 */

package javaproject;

import java.util.HashMap;
import java.util.Map;

public class Main2 {
	
    public static int[] solution(String s) {
        int[] answer = {};
        
        Map<Integer, String[]> map = new HashMap<Integer, String[]>();
        map.put(0, new String[1]);
        int maxCount = 0;
        
        String[] splits = s.substring(2,s.length()-2).split("\\},\\{");
        
        for(String str : splits) {
        	String[] splitStr = str.split(",");
        	map.put(splitStr.length, splitStr);
        	if(maxCount < splitStr.length) {
        		maxCount = splitStr.length;
        	}
        }
        
        answer = new int[maxCount];
        for(int j=1; j<=maxCount;j++) {
        	String[] target = map.get(j);
        	String[] before = map.get(j-1);
        	
        	for(int k=0;k<target.length;k++) {
        		int flag =0;
        		for(int l=0;l<before.length;l++) {
        			if(target[k].equals(before[l])) {
        				flag = 1;
        				break;
        			}
        		}
        		if(flag ==0) {
        			answer[j-1] = Integer.parseInt(target[k]);
        			break;
        		}
        	}
        }
        for(int i=0;i<maxCount;i++) {
        	System.out.print(answer[i] + " ");
        }
        System.out.println();
        return answer;
    }
    
    public static void main(String[] args) {
		solution("{{2},{2,1},{2,1,3},{2,1,3,4}}");
		solution("{{1,2,3},{2,1},{1,2,4,3},{2}}");
		solution("{{20,111},{111}}");
		solution("{{123}}");
		solution("{{4,2,3},{3},{2,3,4,1},{2,3}}");
		
	}
}
