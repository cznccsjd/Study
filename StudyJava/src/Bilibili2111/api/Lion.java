package Bilibili2111.api;

import com.sun.scenario.effect.impl.sw.sse.SSEBlend_ADDPeer;
/*
接口继承接口时，必须实现两个接口中的所有方法
 */
public class Lion implements Manmal{
    public void run(){
        System.out.println("Lion can run");
    }

    public void eat(){
        System.out.println("Lion can eat");
    }

    public String getName(){
        return "Lion";
    }

    public static void main(String[] args){
        Manmal lion = new Lion();
        lion.run();
        lion.eat();
        lion.getName();
    }
}
