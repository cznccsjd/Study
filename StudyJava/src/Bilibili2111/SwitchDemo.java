package Bilibili2111;

public class SwitchDemo {
    public static void main(String[] args){
        int i = 1;
        switch(i){
            case 0:
                System.out.println("case0执行");
            case 1:
                System.out.println("case1执行");      //没搞清楚，为啥没有break，就会继续执行
            case 2:
                System.out.println("case2 running");
                break;
            case 3:
                System.out.println("case3 running");
                break;
        }
    }
}
