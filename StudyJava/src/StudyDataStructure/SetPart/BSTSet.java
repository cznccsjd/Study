package StudyDataStructure.SetPart;

import StudyDataStructure.BSTPart.BST;

public class BSTSet<E extends Comparable<E>> implements Set<E> {  //元素E必须满足可比较的
    //基于BST类的对象
    private BST<E> bst;

    //构造函数
    public BSTSet() {
        bst = new BST<>();
    }

    //Set添加元素
    @Override
    public void add(E e) {
        bst.add(e);
    }

    //移除元素
    @Override
    public void remove(E e) {
        bst.remove(e);
    }

    //返回集合大小
    @Override
    public int getSize() {
        return bst.size();
    }

    //返回集合是否为空
    @Override
    public boolean isEmpty() {
        return bst.isEmpty();
    }

    //是否包含元素
    @Override
    public boolean contains(E e) {
        return bst.contains(e);
    }
}
