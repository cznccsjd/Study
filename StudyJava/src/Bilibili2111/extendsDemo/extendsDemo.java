package Bilibili2111.extendsDemo;

class A{
    A() {
        System.out.println("调用A的构造函数");
    }
    A(int i) {
        System.out.println("调用A的有参构造函数");
    }
}

//类B继承类A
class B extends A{
    B() {
        super(1);  //如果想调用父类的有参构造函数，需要使用super关键字
        System.out.println("调用B的构造函数");
    }
}

public class extendsDemo {
    public static void main(String[] args){
        B b = new B();
    }
}