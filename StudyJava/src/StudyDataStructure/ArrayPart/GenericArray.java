package StudyDataStructure.ArrayPart;

/**
 * 2.泛型数组
 * 前言：通过上一节我们对我们需要封装的数组，进行了基本的增删改查的封装，但只局限于int类型的操作，为了能提供多种类型数组的操作，我们可以将其进一步封装为泛型数组。
 * 1.定义泛型数组相关概念
 *
 * （1）泛型数组让我们可以存放任何数据类型
 *
 * （2）存放的类型不可以是基本数据类型，只能是类对象
 *
 * 基本类型：
 *
 *   boolean、byte、char、short、int、long、float、double
 *
 *
 * （3）每个基本数据类型都有对应的包装类
 *
 *  Boolean、Byte、Char、Short、Integer、Long、Float、Double
 */
public class GenericArray<E> {
    //使用private的目的是防止用户从外界修改，造成数据不一致
    private E[] data;
    private int size;  //数组中元素个数

    //构造函数，传入数组的容量capacity构造Array函数
    public GenericArray(int capacity) {
        data = (E[]) new Object[capacity];  //泛型不能直接实例化
        size = 0;
    }

    //无参构造函数，默认数组的容量 capacity=10
    public GenericArray() {
        this(10);
    }

    //获取数据的容量
    public int getCapacity() {
        return data.length;
    }

    //获取数据是否为空
    public boolean isEmpty() {
        return size == 0;
    }

    //向所有元素后添加元素
    public void addLast(E e) {
        add(size, e);    //size表示此时的最后一个元素
    }

    //在所有元素之前添加一个新元素
    public void addFirst(E e) {
        add(0, e);   //0表示第一个位置
    }

    //在第index个位置插入一个新元素
    public void add(int index, E e) {
        //1.先判断当前数组容量是否已满，未满则转入2，否则抛出异常
        if (size == data.length) {
            throw new IllegalArgumentException("数组已满。");
        }

        //2。判断当前需要插入值的位置是否合理，合理则转入3，否则抛出位置不合法异常
        if (index < 0 || index > size) {
            throw new IllegalArgumentException("您选择的位置不合法！");
        }
        //将index位置之后的元素往后依次移动一位
        for (int i = size - 1; i >= index; i--) {
            //3.将index之后的元素依次往后移动一位，然后将新元素插入到index位置
            data[i + 1] = data[i];
        }
        data[index] = e;
        //4.维护size值
        size++;
    }

    //获取index索引位置的元素
    public E get(int index) {
        //1.判断当前需要插入值的位置是否合理，合理转入2，否则抛出位置不合法异常
        if (index < 0 || index > size) {
            throw new IllegalArgumentException("您选择的位置不合法。");
        }

        //2.返回索引index对应值
        return data[index];
    }

    //获取最后一个元素
    public E getLast() {
        return get(size -1);
    }

    //获取第一个元素
    public E getFirst() {
        return get(0);
    }

    //修改index索引位置的元素为e
    void set(int index, E e) {
        //1.判断当前需要插入值的位置是否合理，合理转入2，否则抛出位置不合法异常
        if (index < 0 || index > size) {
            throw new IllegalArgumentException("您选择的位置不合法");
        }

        //2.修改索引index对应的值
        data[index] = e;
    }

    //查找数组中是否包含元素e
    public boolean contains(E e) {
        for (int i = 0; i < size; i++) {
            if (data[i] == e) {
                return true;
            }
        }
        return false;
    }

    //查找数组中元素e所在的索引（只是一个），如果不存在，则返回-1
    public int find(E e) {
        for (int i = 0; i < size; i++) {
            if (data[i] == e) {
                return i;
            }
        }
        return -1;
    }

    //从数组中删除index位置的元素，返回删除的元素
    public E remove(int index) {
        //1.判断索引的选择是否合法
        if (index < 0 || index > size) {
            throw new IllegalArgumentException("您选择的位置不合法");
        }

        //2.先存储需要删除的索引对应的值
        E ret = data[index];

        //将索引为index之后（index）的元素依次向前移动
        for (int i = index + 1; i < size; i++) {
            //3。执行删除--实质将索引index之后的元素一次向前移动，将元素覆盖
            data[i - 1] = data[i];
        }
        //4.维护size变量值
        size--;
        //手动释放内存
        data[size] = null;
        //5.返回被删除的元素
        return ret;
    }

    //从数组中删除第一个元素，返回被删除的元素
    public E removeFirst() {
        return remove(0);
    }

    //从数组中删除最后一个元素，返回被删除的元素
    public E removeLast() {
        return remove(size -1);
    }

    //从数组中删除元素（只是删除一个）
    public void remeveElement(E e) {
        int index = find(e);
        if (index != -1) {
            remove(index);
        }
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        res.append(String.format("Array:size=%d, capacity=%d\n", size, data.length));
        res.append('[');
        for (int i = 0; i < size; i++) {
            res.append(data[i]);
            if (i != size - 1) {
                res.append(',');
            }
        }
        res.append(']');
        return res.toString();
    }
}
