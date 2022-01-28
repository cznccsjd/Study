package StudyDataStructure.SetPart;

import StudyDataStructure.LinkedListPart.LinkedListWithDummyHead;

public class LinkedListSet<E> implements Set<E> {
    private LinkedListWithDummyHead<E> list;

    public LinkedListSet() {
        list = new LinkedListWithDummyHead<E>();
    }

    @Override
    public void add(E e) {
        if (!list.contains(e)) {
            list.addFirst(e);
        }
    }

    @Override
    public void remove(E e) {
//        list.removeElement(e);    //removeELement方法并不存在，需要看下github源码 https://github.com/FelixBin/dataStructure/blob/master/src/SetPart/LinkedList.java
    }

    @Override
    public int getSize() {
        return list.getSize();
    }

    @Override
    public boolean isEmpty() {
        return list.isEmpty();
    }

    @Override
    public boolean contains(E e) {
        return list.contains(e);
    }
}
