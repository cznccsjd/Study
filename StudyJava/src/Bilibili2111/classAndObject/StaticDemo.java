package Bilibili2111.classAndObject;
/*
static关键字标志的静态变量和静态方法，可以直接用”类名.变量名“或”类名.方法名“来访问；
普通的变量方法访问需要先new一个对象的方式才可以。
 */

import javax.rmi.ssl.SslRMIClientSocketFactory;

public class StaticDemo {
    public static final float PI = 3.14F; //静态常量
    public static int i = 1;   //静态变量
    //静态方法
    public static float yuanmianji(float r){
        return PI*r*r;
    }
    //普通方法
    public float zhouchang(float r){
        return 2*PI*r;
    }

    public static void main(String[] args){
        System.out.println(StaticDemo.i);
        System.out.println(StaticDemo.yuanmianji(1));
        StaticDemo s = new StaticDemo();
        System.out.println(s.zhouchang(1));
        System.out.println(s.yuanmianji(1));
    }
}