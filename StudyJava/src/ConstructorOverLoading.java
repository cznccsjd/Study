public class ConstructorOverLoading {
    public static void main(String[] args){
        PersonOverLoading p1 = new PersonOverLoading();
        PersonOverLoading p2 = new PersonOverLoading("lisi");
        PersonOverLoading p3 = new PersonOverLoading("lisi",20);
    }
}

//构造函数的重载 Overloading
class PersonOverLoading{
    private String name;
    private int age;

    PersonOverLoading(){
        System.out.println("A:name="+name+":::age="+age);
        cry();
    }

    PersonOverLoading(String n){
        name = n;
        System.out.println("B:name="+name+":::age="+age);
        cry();
    }

    PersonOverLoading(String n,int m){
        name = n;
        age = m;
        System.out.println("C:name="+name+":::age="+age);
        cry();
    }

    void cry(){
        System.out.println("Cry...............");
    }
}
