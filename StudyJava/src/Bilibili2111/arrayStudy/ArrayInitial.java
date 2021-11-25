package Bilibili2111.arrayStudy;

public class ArrayInitial {
    public static void main(String[] args){
        //创建一个int型数组
        int[] array1 = new int[3];
        //对数组元素赋值
        array1[0] = 1;
        array1[1] = 2;
        array1[2] = 3;
        //另一种数组创建方式
        int[] array2 = {1,2,3};
//        打印出数组元素
        for(int i=0;i<3;i++){
            System.out.println("array1["+i+"]="+array1[i]);
        }
        for(int i=0;i<3;i++){
            System.out.println("array2["+i+"]="+array2[i]);
        }
        int length1 = array1.length;
        System.out.println("array1的长度是："+length1);
    }
}
