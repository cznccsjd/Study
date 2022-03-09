package StudyStatic;

public class TestForStaticOne extends Base{

    static {
        System.out.println("TestForStaticOne static");
    }

    public TestForStaticOne() {
        System.out.println("TestForStaticOne constructor");
    }

    public static void main(String[] args) {
        new TestForStaticOne();
    }
}

class Base{

    static {
        System.out.println("basic static");
    }

    public Base() {
        System.out.println("Base constructor");
    }
}