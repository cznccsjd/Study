package Bilibili2111.threads;

public class ThreadDemo2 implements Runnable{
    private String name;
    public ThreadDemo2(String name) {
        this.name = name;
    }

    public void run() {
        for(int i=0;i<100;i++) {
            System.out.println(name);
        }
    }

    public static void main(String[] args) {
        Runnable rb1 = new ThreadDemo2("第一个线程");
        Runnable rb2 = new ThreadDemo2("第二个线程");
        Thread td1 = new Thread(rb1);  //其实没搞明白这里的Thread从那里来的？接口Runnable继承的THread？
        Thread td2 = new Thread(rb2);
        td1.start();
        td2.start();
    }
}
