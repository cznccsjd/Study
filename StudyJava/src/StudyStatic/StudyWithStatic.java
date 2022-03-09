package StudyStatic;

public class StudyWithStatic {
    // 静态变量
    private static String strStatic = "staticProperty";
    // 非静态变量
    private String strWithoutStatic = "property";

    public StudyWithStatic() {}

    // 非静态方法
    public void printWithoutStatic() {
        System.out.println("静态变量可以引用：" + strStatic);
        System.out.println("非静态变量可以引用：" + strWithoutStatic);
        // 静态方法可以引用
        printStatic();
        // 非静态方法可以引用
        printWithoutStatic();
    }

    // 静态方法
    public static void printStatic() {
        System.out.println("静态变量可以引用：" + strStatic);
//        System.out.println("非静态变量不可以引用：" + strWithoutStatic);
        // 非静态方法不可以引用
//        printWithoutStatic();
        //静态方法可以引用
        printStatic();
    }

    public static void main(String[] args) {
        // 静态方法，可以直接调用，不需要对象
        printStatic();
        StudyWithStatic studyWithStatic = new StudyWithStatic();
        // 非静态方法，必须有个对象调用，同时这个对象不能调用静态方法
        studyWithStatic.printWithoutStatic();
    }
}
