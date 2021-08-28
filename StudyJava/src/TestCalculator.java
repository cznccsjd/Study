public class TestCalculator {

    public static void main(String[] args) {
        int a = 10;
        int b = 20;
        int c = 25;
        int d = 25;
        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        System.out.println("a * b = " + (a * b));
        System.out.println("b / a = " + (b / a));
        System.out.println("b % a = " + (b % a));
        System.out.println("c % a = " + (c % a));
        System.out.println("a++ = " + (a++));
        System.out.println("a-- = " + (a--));
        // 查看 d++和 ++d的不同
        System.out.println("下面两行代码，查看下d++和++d的区别；当前d的值：" + d);
        System.out.println("d++ = " + (d++));
        System.out.println("++d = " + (++d));
        System.out.println("d++，先进行表达式自增，在进行自增。由于没有表达式，所以");
    }
}
