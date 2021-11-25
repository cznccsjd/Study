package Bilibili2111.api;
/*
内部类
 */
public class Outer {
    String outString = "宿主类的变量";
    void useInner() {
        Inner inner = new Inner();
        inner.print();
    }

//    内部类
    class Inner{
        void print() {
            System.out.println("内部类输出语句");
            System.out.println(outString);
        }
    }

    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.useInner();
    }
}
