package StudyDataStructure.ArrayPart;

/**
 * 3.动态数组
 * 数组容量可变
 */
public class DynamicArray<E> {
    //使用private的目的是防止用户从外界修改，造成数据不一致
    private E[] data;
    private int size;  //数组中元素个数

    //构造函数，传入数组的容量capacity构造Array函数
    public DynamicArray(int capacity) {
        data = (E[]) new Object[capacity];
        size = 0;
    }

    //无参构造函数，默认数组的容量capacity=0
    public DynamicArray() {
        this(0);
    }

    //获取数组中元素个数
    public int getSize() {
        return size;
    }

    //获取数组的容量
    public int getCapacity() {
        return data.length;
    }

    //获取数组是否为空
    public boolean isEmpty() {
        return size == 0;
    }

    //向所有元素后添加元素
    public void addLast(E e) {
        add(size, e); //size表示最后一个元素
    }

    //最开始添加一个元素
   public void addFirst(E e) {
        add(0, e);  //0表示第一个元素
   }

   //在index位置插入一个新元素
    public void add(int index, E e) {
        //1.判断当前需要插入的位置是否合理，合理转入2，不合理抛出位置异常
        if (index < 0 || index > size) {
            throw new IllegalArgumentException("您选择的位置不合法");
        }

        //2.判断当前容量是否已满，满了进行扩容
        if (size == data.length) {
            resize(data.length * 2);
        }

        //3.将index位置之后的元素依次往后移动一位
        for (int i = size -1; i >= index; i--) {
            data[i + 1] = data[i];
        }

        data[index] = e;
        //4.维护size值
        size++;
    }

    //获取index索引位置的元素
    public E get(int index) {
        //1.判断当前查询的位置是否合法，不合法抛出异常
        if (index < 0 || index > size) {
            throw new IllegalArgumentException("您查询的位置不合法");
        }

        //2.返回结果
        return data[index];
    }

    //获取最后一个元素
    public E getLast() {
        return get(size - 1);
    }

    //获取第一个元素
    public E getFirst() {
        return get(0);
    }

  //修改index的值
    public void set(int index, E e) {
        if (index < 0 || index > size) {
            throw new IllegalArgumentException("index位置错误。");
        }

        data[index] = e;
    }

    //查询数组是否包含e
    public boolean contains(E e) {
        for (int i = 0; i < size; i++) {
            if (data[i] == e) {
                return true;
            }
        }
        return false;
    }

    //查询元素e的索引位置，不存在就返回-1
    public int find(E e) {
        for (int i = 0; i < size; i++) {
            if (data[i] == e) {
                return i;
            }
        }
        return -1;
    }

    //从数组中删除index索引的元素，并返回这个元素值
    public E remove(int index) {
        //判断index是否合法
        if (index < 0 || index > size) {
            throw new IllegalArgumentException("index不合法。");
        }

        //获取index的值
        E ret = data[index];

        //把index及其后面的元素，往前提1位
        for (int i = index; i < size - 1; i++) {
            data[i] = data[i + 1];
        }

        //数组长度-1
        size --;
        //手动释放内存空间
        data[size] = null;

        //缩容操作
        if (size == data.length / 4 && data.length != 0) {    //把这里的data.length / 2 改为 data.length / 4，目的是降低removeLast()的时间复杂度，参考TestDynamicArrayForLazy.java文件
            resize(data.length / 2);
        }
        return ret;
    }

    //从数组中删除第一个元素，返回被删除的元素
    public E removeFirst() {
        return remove(0);
    }

    //从数组中删除最后一个元素，返回被删除的元素
    public E removeLast() {
        return remove(size - 1);
    }

    //从数组中删除一个元素
    public void removeElement(E e) {
        int index = find(e);
        if (index != -1) {
            remove(index);
        }
    }

    //数组扩容
    private void resize(int newCapacity) {
        E[] newData = (E[]) new Object[newCapacity];
        int num = 0;    //配合TestDynamicArrayByJlz使用

        for (int i = 0; i < size; i++) {
            num++;
            newData[i] = data[i];
        }

        System.out.println("数组扩容，循环了" + num + "次。");    //配合TestDynamicArrayByJlz使用

        data = newData;
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        res.append(String.format("Array:size=%d, capacity=%d\n", size, data.length));
        res.append("[");
        for (int i = 0; i < size; i++) {
            res.append(data[i]);
            if (i != size - 1) {
                res.append(",");
            }
        }
        res.append("]");
        return res.toString();
    }
}
