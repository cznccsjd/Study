import java.io.*;

public class EmployeeTest {
    public static void main(String[] arggs){
//        使用构造器创建两个对象
        Employee empOne = new Employee("jlz1");
        Employee empTwo = new Employee("jlz2");

//        调用这两个对象的成员方法
        empOne.empAge(26);
        empOne.empDesignation("高级开发");
        empOne.empSalary(33000);
        empOne.printEmployee();

        empTwo.empAge(32);
        empTwo.empDesignation("中级测试");
        empTwo.empSalary(16000);
        empTwo.printEmployee();
    }
}
