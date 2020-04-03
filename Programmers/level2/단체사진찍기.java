/**
 * 
 * [문제 설명]
	단체사진 찍기
	picture
	
	가을을 맞아 카카오프렌즈는 단체로 소풍을 떠났다. 즐거운 시간을 보내고 마지막에 단체사진을 찍기 위해 카메라 앞에 일렬로 나란히 섰다. 그런데 각자가 원하는 배치가 모두 달라 어떤 순서로 설지 정하는데 시간이 오래 걸렸다. 네오는 프로도와 나란히 서기를 원했고, 튜브가 뿜은 불을 맞은 적이 있던 라이언은 튜브에게서 적어도 세 칸 이상 떨어져서 서기를 원했다. 사진을 찍고 나서 돌아오는 길에, 무지는 모두가 원하는 조건을 만족하면서도 다르게 서는 방법이 있지 않았을까 생각해보게 되었다. 각 프렌즈가 원하는 조건을 입력으로 받았을 때 모든 조건을 만족할 수 있도록 서는 경우의 수를 계산하는 프로그램을 작성해보자.
	
	입력 형식
	입력은 조건의 개수를 나타내는 정수 n과 n개의 원소로 구성된 문자열 배열 data로 주어진다. data의 원소는 각 프렌즈가 원하는 조건이 N~F=0과 같은 형태의 문자열로 구성되어 있다. 제한조건은 아래와 같다.
	
	1 <= n <= 100
	data의 원소는 다섯 글자로 구성된 문자열이다. 각 원소의 조건은 다음과 같다.
	첫 번째 글자와 세 번째 글자는 다음 8개 중 하나이다. {A, C, F, J, M, N, R, T} 각각 어피치, 콘, 프로도, 제이지, 무지, 네오, 라이언, 튜브를 의미한다. 첫 번째 글자는 조건을 제시한 프렌즈, 세 번째 글자는 상대방이다. 첫 번째 글자와 세 번째 글자는 항상 다르다.
	두 번째 글자는 항상 ~이다.
	네 번째 글자는 다음 3개 중 하나이다. {=, <, >} 각각 같음, 미만, 초과를 의미한다.
	다섯 번째 글자는 0 이상 6 이하의 정수의 문자형이며, 조건에 제시되는 간격을 의미한다. 이때 간격은 두 프렌즈 사이에 있는 다른 프렌즈의 수이다.
	출력 형식
	모든 조건을 만족하는 경우의 수를 리턴한다.
	
	예제 입출력
	n	data	answer
	2	[N~F=0, R~T>2]	3648
	2	[M~C\<2, C~M>1]	0
	예제에 대한 설명
	첫 번째 예제는 문제에 설명된 바와 같이, 네오는 프로도와의 간격이 0이기를 원하고 라이언은 튜브와의 간격이 2보다 크기를 원하는 상황이다.
	
	두 번째 예제는 무지가 콘과의 간격이 2보다 작기를 원하고, 반대로 콘은 무지와의 간격이 1보다 크기를 원하는 상황이다. 이는 동시에 만족할 수 없는 조건이므로 경우의 수는 0이다.
 * 
 * 
 * [문제풀이] : 함수 내에서 전역변수에 대한 초기화 코드가 필요함. (문제 주의사항)
 * 
 * 사람 수가 8명밖에 안되므로 완전탐색의 시간복잡도가 8!밖에 안된다. 따라서 완전탐색으로 접근한다.
 * 
 *  A,C,F,J,M,N,R,T를 다루기 쉽게 0~7로 각각 매핑해서 사용한다.
 *  
 *  주의1. int[] permutation 배열의 의미를 명확히 하는 것이 좋다.
 *  permutation의 index의 의미와 value의 의미를 명확히 해야 한다.
 *  index : 자리, value : 위치 로 정의할 경우, 
 */

package javaproject;

import java.util.HashMap;
import java.util.Map;

public class Main {

//	static int[] permutation = new int[8];
	static Map<Character, Integer> map;
	static int answer;

	public static int solution(int n, String[] data) {
		map = new HashMap<Character, Integer>();
		answer = 0;
		map.put('A', 0);
		map.put('C', 1);
		map.put('F', 2);
		map.put('J', 3);
		map.put('M', 4);
		map.put('N', 5);
		map.put('R', 6);
		map.put('T', 7);

		int[] permutation = new int[8];

		dfs(0, permutation, data, 0);

		return answer;
	}

	// 인덱스 : 자리, 값 : 사람
	// 인덱스 : 사람, 값 : 자리 --> 이 방식이 더 적합함.
	private static void dfs(int depth, int[] permutation, String[] data, int visited) {
		if (depth == 8) {
			int c1, c2, dist;
			char compare;
			for (String d : data) {
				c1 = permutation[map.get(d.charAt(0))]; // 위치를 반환 (1)
				c2 = permutation[map.get(d.charAt(2))]; // 위치를 반환 (3)
				compare = d.charAt(3);
				dist = d.charAt(4) - '0';

				if (compare == '>') {
					if (Math.abs(c2 - c1) - 1 <= dist)
						return;
				} else if (compare == '<') {
					if (Math.abs(c2 - c1) - 1 >= dist)
						return;
				} else if (compare == '=') {
					if (Math.abs(c2 - c1) - 1 != dist)
						return;
				}
			}
			answer++;
			return;
		}
		// 00000010 : 1번 자리에 사람이 서있다는 뜻.
		for (int i = 0; i < 8; i++) {
			if (((visited >> i) & 1) == 0) {
				permutation[depth] = i;
				dfs(depth + 1, permutation, data, visited | (1 << i));
			}
		}
	}

	public static void main(String[] args) {
		String[] data = { "N~F=0", "R~T>2" };
		System.out.println(solution(2, data));
	}
}
