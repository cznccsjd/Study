package StudyDataStructure.StackPart;

import StudyDataStructure.LinkedListPart.LinkedListWithDummyHead;

/**
 * 基于链表实现栈
 */

public class LinkedListStack<E> implements Stack<E> {
//    private LinkedList<E> list;
    private LinkedListWithDummyHead<E> list;

    public LinkedListStack() {
        list = new LinkedListWithDummyHead<E>();
    }

    //栈中元素个数
    @Override
    public int getSize() {
        return list.getSize();
    }

    //栈中是否为
    @Override
    public boolean isEmpty() {
        return list.isEmpty();
    }

    //在栈中添加元素
    @Override
    public void push(E e) {
        list.addFirst(e);                 ///################这里的进栈，怎么是添加到第一个元素，不应该是最后一个吗？？？？？？？？？？？
    }

    //从栈中删除第一个元素
    @Override
    public E pop() {
        return list.removeFirst();    //##########栈，删除的时候，不应该删除最后一个元素吗？？？
    }

    //查看栈中的第一个元素
    @Override
    public E peek() {
        return list.getFirst();
    }

    //主要是便于输出给对象信息
    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        res.append("Stack: top ");
        res.append(list);
        return res.toString();
    }
}
