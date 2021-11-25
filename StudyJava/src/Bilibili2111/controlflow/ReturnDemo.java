package Bilibili2111.controlflow;

public class ReturnDemo {
    public static int returnSomething(){
        for(int i=0;i<5;i++){
            if(i==3){
                return i;
            }
        }
        return 0;
    }

    public static void main(String[] args){
        int n = returnSomething();
        System.out.println(n);
    }
}
