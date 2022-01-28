package StudyDataStructure.ArrayPart;

public class TestArrayMain {
    public static void main(String[] args) {
        //测试toString()方法
        Array testArray = new Array(20);
        for (int i = 0; i < 10; i++) {
            //测试addLast(int e)方法
            testArray.addLast(i);
        }
        System.out.println("添加数组元素：");
        System.out.println(testArray);

        //测试add(int index, int e)方法
        testArray.add(1, 200);
        System.out.println("在数组指定索引位置插入元素：");
        System.out.println(testArray);

        //测试addFirst(int e)方法
        testArray.addFirst(-10);
        System.out.println("在数组头部插入元素：");
        System.out.println(testArray);

        //测试get(int index)方法
        System.out.println("根据数组索引查找数组元素：");
        System.out.println(testArray.get(11));

        //测试set()方法
        testArray.set(11, 1000);
        System.out.println("修改数组索引位置上元素值：");
        System.out.println(testArray.get(11));

        //测试remove(index)方法
        System.out.println(testArray);
        testArray.remove(0);
        System.out.println("删除数组中指定index元素：");
        System.out.println(testArray);

        //测试reomveFirst()方法
        System.out.println(testArray);
        System.out.println("删除数组中第一个元素：");
        testArray.removeFirst();
        System.out.println(testArray);

        //测试removeLast()方法
        System.out.println("删除数组最后一个元素：");
        testArray.removeLast();
        System.out.println(testArray);

        //测试removeElement(int e)方法
        System.out.println("测试removeElement()方法：");
        testArray.removeElement(5);
        System.out.println(testArray);

        //测试contains(int e)方法：
        System.out.println("测试contains()方法：");
        System.out.println(testArray.contains(5));

        //测试find(int e)方法
        System.out.println("元素e在数组中的索引：");
        int index = testArray.find(2);
        System.out.println("index = " + index);
    }
}
