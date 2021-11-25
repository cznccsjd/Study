package Bilibili2111.classAndObject;

public class OverLoadDemo {
    public void method(){
        System.out.println("无参数方法被调用");
    }

    public void method(int a){
        System.out.println("参数为int类型被调用");
    }

    public void method(String a){
        System.out.println("参数为String类型被调用");
    }

    public void method(String a,String b){
        System.out.println("俩参数为String类型被调用");
    }

    public static void main(String[] args){
        OverLoadDemo overLoadDemo = new OverLoadDemo();
        overLoadDemo.method();
        overLoadDemo.method(1);
        overLoadDemo.method("haha");
        overLoadDemo.method("hello","world");
    }
}
