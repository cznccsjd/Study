/*
在使用 StringBuffer 类时，每次都会对 StringBuffer 对象本身进行操作，而不是生成新的对象，所以如果需要对字符串进行修改推荐使用 StringBuffer。

StringBuilder 类在 Java 5 中被提出，它和 StringBuffer 之间的最大不同在于 StringBuilder 的方法不是线程安全的（不能同步访问）。

由于 StringBuilder 相较于 StringBuffer 有速度优势，所以多数情况下建议使用 StringBuilder 类。
 */
public class TestStringBuffer {
    public static void main(String[] args){
        StringBuilder sb = new StringBuilder(10);
        sb.append("jlz");
        System.out.println(sb);
        sb.append("!");
        System.out.println(sb);
        sb.insert(4, "java");
        System.out.println(sb);
        sb.delete(2,4);
        System.out.println(sb);
    }
}
