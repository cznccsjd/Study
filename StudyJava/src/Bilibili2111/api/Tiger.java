package Bilibili2111.api;

public class Tiger implements Animal{
    public void eat(){
        System.out.println("老虎吃肉");
    }

    public String getName(){
        return "老虎";
    }

    public static void main(String[] args){
        Animal tiger = new Tiger();
//        Tiger tiger = new Tiger();
        tiger.eat();
        System.out.println(tiger.getName());
    }
}
