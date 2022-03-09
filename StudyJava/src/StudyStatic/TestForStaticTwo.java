package StudyStatic;

public class TestForStaticTwo {
    Person person = new Person("TestForStaticTwo");

    static {
        System.out.println("TestForStaticTwo static");
    }

    public TestForStaticTwo() {
        System.out.println("TestForStaticTwo constructor");
    }

    public static void main(String[] args) {
        new MyClass();
    }
}

class Person {
    static {
        System.out.println("Person static");
    }

    public Person(String str) {
        System.out.println("Person " + str);
    }
}

class MyClass extends TestForStaticTwo {
    Person person = new Person("MyClass");

    static {
        System.out.println("myclass static");
    }

    public MyClass() {
        System.out.println("myclass constructor");
    }
}