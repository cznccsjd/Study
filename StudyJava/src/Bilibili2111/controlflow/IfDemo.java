package Bilibili2111.controlflow;

public class IfDemo {
    public static void ifDemo() {
        int a=1;
        int b=2;
        if(a<b) {
            System.out.println("a小于b");
        }else{
            System.out.println("a大于b");
        }
    }

    public static void ifElseDemo() {
        int a=1;
        int b=2;
        if(a<b) {
            if(a<b-1) {
                System.out.println("a小于b-1");
            }else{
                System.out.println("a小于b，但不小于b-1");
            }
        }else{
            System.out.println("a不小于b");
        }
    }

    public static void ifJietiDemo() {
        String s = "星期一";
        if(s.equals("星期六")){
            System.out.println("今天是星期六");
        }else if(s.equals("星期天")){
            System.out.println("今天是星期天");
        }else{
            System.out.println("今天不是周末");
        }
    }

    public static void main(String[] args) {
//        ifElseDemo();
        ifJietiDemo();
    }
}
