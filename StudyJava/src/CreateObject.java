public class CreateObject {
    /*
    创建对象：
    对象是跟进类创建的，在Java中，使用关键字new来创建一个新的对象。创建对象需要一下三步：
    声明：声明一个对象，包括对象名称和对象类型；
    实例化：使用关键字new来创建一个对象；
    初始化：使用new创建对象时，会调用构造方法初始化对象；
     */
    public CreateObject(String name){
//        创建的构造器，并且这个构造器只有一个参数：name
        System.out.println("这个新建的对象名：" + name);
    }
    public static void main(String[] args){
//        下面的语句创建一个CreateObject对象
        CreateObject myObject = new CreateObject("Car");
    }
}
