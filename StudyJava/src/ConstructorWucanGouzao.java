public class ConstructorWucanGouzao {
    public static void main(String[] args){
//        下面的new对象一建立，就会调用对应的构造函数Construct()，并执行其中的println语句
        Construct c1 = new Construct();
    }
}

class Construct{
//    定义一个无参构造函数
    Construct(){
        System.out.println("这是一个无参构造函数");
    }
}