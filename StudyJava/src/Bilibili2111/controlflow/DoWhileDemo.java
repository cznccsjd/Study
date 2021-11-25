package Bilibili2111.controlflow;

public class DoWhileDemo {
    public static void main(String[] args){
        int n=5;   //定义一个int变量
        do {
            System.out.println("n=" + n);
            n--;    //n值-1
        }while(n>0);
    }
}
