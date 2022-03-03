package Algorithm;

/**
 * 归并排序
 */

public class MergeSort {
    public static void mergeSort(int[] array, int start, int end) {
        if (start < end) {
            // 折半成两个小集合，分别进行递归
            int mid = (start + end) / 2;
            mergeSort(array, start, mid);
            mergeSort(array, mid+1, end);
            // 把两个有序小集合，归并成一个大集合
            merge(array, start, mid, end);
        }
    }

    public static void merge(int[] array, int start, int mid, int end) {
        // 开辟额外大集合，设置指针
        int [] tmpArray = new int[end-start+1];
        int p1 = start;
        int p2 = mid + 1;
        int p = 0;
        // 比较两个小集合的元素，依次放入大集合
        while (p1 <= mid && p2 <= end) {
            if (array[p1] <= array[p2]) {
                tmpArray[p++] = array[p1++];
            } else {
                tmpArray[p++] = array[p2++];
            }
        }
        // 左侧小集合还有剩余，依次放入大集合尾部
        while (p1 <= mid) {
            tmpArray[p++] = array[p1++];
        }
        // 右侧小集合还有剩余，依次放入大集合尾部
        while (p2 <= end) {
            tmpArray[p++] = array[p2++];
        }
        // 把大集合的元素复制回原数组
        for (int i=0; i<tmpArray.length; i++) {
            array[i+start] = tmpArray[i];
        }
    }

    public static void main(String[] args) {
        RadomList randomList = new RadomList(15);
        int[] testArray = randomList.setRadomList();
        System.out.println("原始数组：" + randomList);
        mergeSort(testArray, 0, testArray.length-1);
        // 打印最新的数组
        System.out.println("MergeSort后的数组：" + randomList);
    }
}