package Bilibili2111.classAndObject;

public class Human {
    //声明各类变量来描述类的属性
    private String name;
    private String sex;
    private int age;

    public void work(){
        System.out.println("我在工作");
    }

    public void eat(){
        System.out.println("我在吃饭");
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name=name;
    }

    public String getSex(){
        return sex;
    }

    public void setSex(String sex){
        this.sex = sex;
    }

    public int getAge(){
        return age;
    }

    public void setAge(int age){
        this.age = age;
    }

    public static void main(String[] args){
        Human zhangsan = new Human();
        Human lisi = zhangsan;
        System.out.println(zhangsan.getName());
        zhangsan.setName("张三");
        System.out.println(zhangsan.getName());
        System.out.println(lisi.getName());
    }
}
