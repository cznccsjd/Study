package Bilibili2111.threads;

public class ThreadDemo3 {
    public static void main(String[] args) {
        new Thread() {
            public void run() {
                int i = 5;
                while(i>0) {
                    System.out.println("i="+i);
                    try {
                        Thread.sleep(1000);
                    }catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    i--;
                }
                System.out.println("线程执行了");
            }
        }.start();
        System.out.println("线程外");
    }
}
