/*
static 修饰符
静态变量：
static 关键字用来声明独立于对象的静态变量，无论一个类实例化多少对象，它的静态变量只有一份拷贝。 静态变量也被称为类变量。局部变量不能被声明为 static 变量。

静态方法：
static 关键字用来声明独立于对象的静态方法。静态方法不能使用类的非静态变量。静态方法从参数列表得到数据，然后计算这些数据。
 */

public class InstanceCounter {
    private static int numInstances = 0;    // static修饰静态变量
    protected static int getCount() {
        return numInstances;
    }

    private static void addInstance() {
        numInstances++;
    }

    InstanceCounter() {
        InstanceCounter.addInstance();
        System.out.println("after new InstanceCount, num is " + InstanceCounter.getCount());
    }

    public static void main(String[] arguments){
        System.out.println("Starting with " +
                InstanceCounter.getCount() +
                " instances");

        for (int i = 0; i < 500; ++i){      // 局部变量不能被声明为static变量
            System.out.println("Now i = " + i);
            new InstanceCounter();
        }

        System.out.println("Created " + InstanceCounter.getCount() + " instances");
    }
}
