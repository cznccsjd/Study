package Bilibili2111.extendsDemo;
/*
覆写override，可以重写一个和父类中方法名参数都一样的方法，在子类中调用该方法时，
将会调用子类里重写的这个方法，要想在调用父类中的方法，只能用super关键字才可以。
 */

class Parent{
     void method(){
         System.out.println("父类中的方法");
     }
}

class Child extends Parent{
     void method() {
         super.method();   //使用super关键字，调用父类中的方法
         System.out.println("子类中的方法");
     }
}

public class OverrideDemo {
     public static void main(String[] args){
         Child child = new Child();
         child.method();
     }
}
