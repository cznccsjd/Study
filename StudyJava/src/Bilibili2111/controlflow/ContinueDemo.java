package Bilibili2111.controlflow;

public class ContinueDemo {
    public static void main(String[] args){
        for(int i=1;i<6;i++){
            System.out.println(i+"");
//            当i不能整除5的时候继续循环
            if(i%5!=0){
                continue;
            }
            System.out.println("**********");
        }
    }
}
