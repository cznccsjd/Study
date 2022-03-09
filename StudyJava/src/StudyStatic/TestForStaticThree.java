package StudyStatic;

public class TestForStaticThree {
    static {
        System.out.println("Test static 1");
    }

    public static void main(String[] args) {
    }

    static {
        System.out.println("test static 2");
    }
}
