package StudyDataStructure.ArrayPart;

public class QuickStart {
    public static void main(String[] args) {
        int[] arr = new int[10];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i;
            System.out.println(arr[i]);
        }
        System.out.println("查询第5个元素的值为：" + arr[4]);
        System.out.println("====================");

        int[] scores = new int[]{100, 99, 98};
        for (int i = 0; i < scores.length; i++) {
            System.out.println(scores[i]);
        }
        System.out.println("====================");

        for (int score: scores) {
            System.out.println(score);
        }
        System.out.println("====================");

        scores[0] = 96;
        for (int i = 0; i < scores.length; i++) {
            System.out.println(scores[i]);
        }
    }
}
