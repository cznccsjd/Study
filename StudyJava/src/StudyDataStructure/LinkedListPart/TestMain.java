package StudyDataStructure.LinkedListPart;

public class TestMain {
    public static void main(String[] args) {
        LinkedListWithDummyHead<Integer> linkedListWithDummyHead = new LinkedListWithDummyHead<Integer>();

        System.out.println("============在链表头部添加==============");
        for (int i = 0; i < 5; i++) {
            linkedListWithDummyHead.addFirst(i);
            System.out.print(linkedListWithDummyHead);
            System.out.println('\n');
        }

        System.out.println("===========修改链表================");
        linkedListWithDummyHead.set(3, 666);
        System.out.println(linkedListWithDummyHead);

        System.out.println("============删除某个链表元素================");
        linkedListWithDummyHead.remove(4);
        System.out.println(linkedListWithDummyHead);
    }
}
