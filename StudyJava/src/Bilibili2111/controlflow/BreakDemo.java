package Bilibili2111.controlflow;

public class BreakDemo {
    public static void main(String[] args){
        for(int i=0;i<20;i++){
            System.out.println("i="+i);
            //当i=10时跳出循环语句
            if(i==10){
                break;
            }
        }
        System.out.println("循环跳出");
    }
}
