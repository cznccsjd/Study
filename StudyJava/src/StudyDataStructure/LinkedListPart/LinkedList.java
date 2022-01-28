package StudyDataStructure.LinkedListPart;

public class LinkedList<E> {
    //将Node节点设计成私有的类中类
    private class Node<E> {
        public E e;    //数据域
        public Node next;    //指向下一个节点

//        两个参数的构造函数
        public Node(E e, Node next) {
            this.e = e;
            this.next = next;
        }

//        一个参数的构造函数
        public Node(E e) {
            this.e = e;
            this.next = null;
        }

//        无参构造函数
        public Node() {
            this(null, null);
        }

        @Override
        public String toString() {
            return e.toString();
        }
    }

//    定义头节点
    private Node head;

//    节点个数
    private int size;

//    无参数构造函数
    public LinkedList() {
        head = null;
        size = 0;
    }

//    获取链表中的元素个数
    public int getSize() {
        return size;
    }

//    返回链表是否为空
    public boolean isEmpty() {
        return size == 0;
    }

//    在链表头添加新的元素e
    public void addFirst(E e) {
        Node node = new Node(e);
        node.next = head;
        head = node;

        size++;
    }

//    在链表的index(0--based)的位置添加新的元素e  (实际不常用，练习用)
    public void add(int index, E e) {
        if (index < 0 || index > size) {
            throw new IllegalArgumentException("位置不合法");
        }

//        对于头节点的特殊处理
        if (index == 0) {
            addFirst(e);
        }else {
            Node prev = head;
            for (int i = 0; i < index - 1; i++) {
//                获取到需要添加元素位置的前一个元素
                prev = prev.next;
            }

            Node node = new Node(e);
            node.next = prev.next;
            prev.next = node;

            size++;
        }
    }

//    在链表尾部添加元素
    public void addLast(E e) {
        add(size, e);
    }
}