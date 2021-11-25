package Bilibili2111.exceptions;

public class TryCatchDemo {
    public static void main(String[] args){
        String str = null;
        int strLength = 0;
        try {
            strLength = str.length();
        }catch (NullPointerException e){
            e.printStackTrace();
        }
        System.out.println(strLength);
    }
}
