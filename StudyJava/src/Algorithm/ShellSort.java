package Algorithm;

import java.util.Random;

/**
 * 希尔排序
 */

public class ShellSort {
    private int N;
    private static void shellSort(int[] arr) {
        int N = arr.length;
        // 进行分组，最开始时的增量（gap）为数组长度一半
        for (int gap = N/2; gap > 0; gap /= 2) {
            // 对各个分组进行插入排序
            for (int i = gap; i < N; i++) {
                // 将arr[i]插入到所在分组的正确位置
                insertI(arr, gap, i);
            }
        }
    }

    private static void insertI(int[] arr, int gap, int i) {
        int inserted = arr[i];
        int j;
        // 插入的时候按组进行插入（组内元素两两相隔gap）
        for (j = i-gap; j >=0 && inserted < arr[j]; j -= gap) {
            if (gap == 2 && i == 11) {
                System.out.println("这里观察下9怎么跑的");
            }
            arr[j+gap] = arr[j];
        }
        arr[j+gap] = inserted;
    }

    public static void main(String[] args) {
//        RadomList randomList = new RadomList();
//        int[] testArr = randomList.setRadomList();
//        System.out.println("希尔排序前的数组：" + randomList);
//        System.out.println("randomList的变量类型：" + randomList.getClass().toString());
//        System.out.println("testArr的类型：" + testArr.getClass().toString());
//        shellSort(testArr);
//        System.out.println("希尔排序后的数组：" + randomList);
//        System.out.println("shellSort：" + testArr);

        int[] testArr = {5,7,8,3,91,22,4,6,12,66,19,88,1,21,74,9,34};
        shellSort(testArr);
        System.out.println("shellSort:");
        StringBuilder res = new StringBuilder();
        res.append('[');
        for (int i = 0; i < testArr.length; i++) {
//            System.out.println(testArr[i]);
            res.append(testArr[i]);
            if (i != testArr.length - 1) {
                res.append(',');
            }
        }
        res.append(']');
        System.out.println(res.toString());
    }
}
