package Bilibili2111.extendsDemo;
/*
多态
 */

class P{
    void method() {
        System.out.println("父类中的method");
    }
}

class C extends P{
    void method() {
        System.out.println("子类中的method");
    }

    void method1() {
        System.out.println("子类中的method1");
    }
}

public class Duotai {
    public static void main(String[] args){
        P c = new C();
        c.method();
        ((C) c).method1();
//        c.method1();    //这样写执行不了，目前还理解不了
    }
}
