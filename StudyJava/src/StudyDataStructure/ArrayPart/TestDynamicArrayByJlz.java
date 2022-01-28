package StudyDataStructure.ArrayPart;

public class TestDynamicArrayByJlz {
    public static void main(String[] args) {
        DynamicArray<Integer> arr = new DynamicArray<Integer>(8);

        for (int i = 1; i <= 9; i++) {
//            arr.addLast(i);
            System.out.println("新增第" + i + "个元素：");
            arr.addLast(i);
            System.out.println(arr);
        }

//        System.out.println("初始化后的数组为：");
//        System.out.println(arr);
//
//        System.out.println("新增一个元素：");
//        arr.addLast(9);
//        System.out.println(arr);
//
//        System.out.println("新增第二个元素");
//        arr.addLast(10);
//        System.out.println(arr);
//
//        System.out.println("新增第三个元素");
//        arr.addLast(11);
//        System.out.println(arr);
//
//        System.out.println("新增第四个元素：");
//        arr.addLast(12);
//        System.out.println(arr);

//        for (int i = 1; i <= 9; i++) {
//            System.out.println("新增第" + i + "个元素：");
//            arr.addLast(i);
//            System.out.println(arr);
//        }
    }
}
