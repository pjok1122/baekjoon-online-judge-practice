//입력 : [1], [2] --> 출력 1
//입력 : [2], [1] --> 출력 0
//입력 : [1,2,3], [3,2] --> 출력 2

public class main {
    public static int solution(int[] goods, int[] boxes) {
        int answer = 0;

        Arrays.sort(goods);
        Arrays.sort(boxes);

        int start = 0;

        for (int i = 0; i < goods.length; i++) {
            int target = goods[i];

            for (int j = start; j < boxes.length; j++) {
                int box = boxes[j];

                if (target >= box) {
                    answer++;
                    start = j;
                    break;
                }
            }
        }

        return answer;
    }
}