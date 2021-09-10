public class ContructorYoucanGouzao {
    public static void main(String[] args) {
//        new对象，并且调用show()方法
        Person z = new Person("Zhangsan", 30);
        z.show();

//        new对象，这个对象的构造方法直接带了输出
        Personal j = new Personal("lisi", 20);

//    构造函数只能运行一次，我们可以使用get和set方法，重新给对象赋值
        MyPerson l = new MyPerson("Wangwu", 18);
        l.setName("Zhaoliu");
        l.print();
    }

}

class Person{
    private String name;
    private int age;
//    这是一个有参构造函数
    public Person(String n,int m){
        name = n;
        age = m;
    }

//    getter
    public String getName(){
        return name;
    }

    public int getAge(){
        return age;
    }

    public void show(){
        System.out.println(name+"\n"+age);
    }
}

class Personal{
    private String name;
    private int age;

    public Personal(String n,int m){
        name = n;
        age = m;
        System.out.println(name+";\n"+age);
    }
}

class MyPerson{
    private String name;
    private int age;

    public MyPerson(String n,int m){
        name = n;
        age = m;
        System.out.println(name+"\n"+age);
    }

    public String getName(){
        return name;
    }

    public void setName(String x){
        name = x;
    }

    public void print(){
        System.out.println("哈哈哈，修改后的名字和年龄；"+name+";"+age);
    }
}