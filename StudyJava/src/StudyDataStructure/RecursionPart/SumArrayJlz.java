package StudyDataStructure.RecursionPart;

/**
 * 1、递归函数就是一个函数，完成一个功能，自己调用自己。
 * 2、宏观语意为问题更小的子过程。
 */
public class SumArrayJlz {
    public static int sum(int[] arr) {
        return sum(arr, 0);  //默认index从0开始
    }

    //定义一个方法，实现数组相加功能
    private static int sum(int[] arr, int i) {
        //结束条件
        if (i == arr.length) {
            return 0;
        }

        return arr[i] + sum(arr, i+1);
    }

    //测试方法
    public static void main(String[] args) {
        int[] nums = {0, 1, 2, 3, 4, 5, 6, 7, 8};
        int value = sum(nums);
        System.out.println(value);
    }
}
