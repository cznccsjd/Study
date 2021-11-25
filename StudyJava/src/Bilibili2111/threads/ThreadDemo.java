package Bilibili2111.threads;

public class ThreadDemo extends Thread{
    private String name;

    public ThreadDemo(String name){
        this.name = name;
    }

    public void run() {
        for (int i = 0; i < 100; i++) {
            System.out.println(name);
        }
    }

    public static void main(String[] args){
        ThreadDemo td1 = new ThreadDemo("第一个线程");
        ThreadDemo td2 = new ThreadDemo("第二个线程");
        ThreadDemo td3 = new ThreadDemo("第三个线程");
        td1.start();
        td2.start();
        td3.start();
    }
}
