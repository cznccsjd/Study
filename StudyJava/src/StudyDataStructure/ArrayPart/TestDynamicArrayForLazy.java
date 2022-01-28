package StudyDataStructure.ArrayPart;

/**
 * 验证涉及resize() 复杂度产生震荡的原因
 * 主要验证点：data.length = capacity时，新插入一位，addLast()的时间复杂度为O(n);如果数组data.length != capacity时，addLast()的时间复杂度为O(1);
 * 数组data.length = capacity/2 + 1时，removeLast()的时间复杂度为O(n);如果数组data.length != capacity/2 + 1，removeLast()的时间复杂度为O(1);
 */

public class TestDynamicArrayForLazy {
    public static void main(String[] args) {
        DynamicArray<Integer> arr = new DynamicArray<Integer>(10);
        for (int i = 1; i <= 10; i++) {
            arr.addLast(i);
        }

        //参考文档：https://www.cnblogs.com/wfaceboss/p/10619785.html
        System.out.println("测试前，记得修改StudyArrayAndLinkedList/Array/DynamicArray.java:140,将" +
                "if (size == data.length / 4 && data.length != 0) { 改为 /2 或 /4");

        System.out.println("此时数组的元素是：");
        System.out.println(arr);

        System.out.println("#######################################");
        System.out.println("此时数组长度为：" + arr.getSize() + ";" +
                "数组再加一位，会触发resize扩容，addLast()的时间复杂度变为O(n);");
        arr.addLast(1);
        System.out.println(arr);

        System.out.println("#######################################");
        System.out.println("此时数组的长度为：" + arr.getSize() + ";" +
                "调用removeLast(),会触发resize扩容，导致removeLast()的时间复杂度变为O(n);");
        for (int i = 1; i <= 6; i++) {
            arr.removeLast();
        }

        System.out.println(arr);

    }
}
