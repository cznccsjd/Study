package Algorithm;

import java.util.Random;

/**
 * 生成随机列表
 */

public class RadomList {
    private int[] arr;
    private int len;
    private int size;

    public RadomList(int capacity) {
        arr = new int[capacity];
        this.size = capacity;
        len = 0;
    }

    public RadomList() {
        this(10);
    }

    public int[] setRadomList() {
//        int[] arr = new int[len];
        for(int i = 0; i < size; i++) {
            Random random = new Random();
            int num = random.nextInt(50);
            ++num;
            arr[i] = num;
            ++len;
        }
        return arr;
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        res.append('[');
        for(int i = 0; i < len; i++) {
            res.append(arr[i]);
            if (i != len - 1) {
                res.append(',');
            }
        }
        res.append(']');
        return res.toString();
    }

    public static void main(String[] args) {
        RadomList randomList = new RadomList(15);
        randomList.setRadomList();
        System.out.println(randomList.toString());
    }
}
