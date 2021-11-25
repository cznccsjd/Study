/*
String 创建的字符串存储在公共池中，而 new 创建的字符串对象在堆上：    参考：https://www.runoob.com/java/java-string.html
 */
public class TestString {
    public static void main(String[] args){
        String str1 = "Runoob1";
        String str2 = "Runoob2";
        String str3 = str1;
        String str4 = new String("Runooob4");
        String str5 = new String("Runoob5");
        System.out.println("str1,str2,str3在公共池中；str4,str5在堆中");
        System.out.println(str1);
        System.out.println(str2);
        System.out.println(str3);
        System.out.println(str4);
        System.out.println(str5);
        System.out.println("str1的长度：" + str1.length());

//        定义一个数组
        char[] helloArray = {'r', 'u', 'n', 'o', 'o', 'b'};
        String helloString = new String(helloArray);
        System.out.println("新定义的数组为" + helloString);
        System.out.println("helloArray的数据类型：" + helloArray.getClass().toString());      //这个的数据类型：class [c 不懂什么意思。。。
        System.out.println("helloString的数据类型：" + helloString.getClass().toString());
    }
}
