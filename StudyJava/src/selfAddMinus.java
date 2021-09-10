/*
前缀自增自减法(++a,--a): 先进行自增或者自减运算，再进行表达式运算。

后缀自增自减法(a++,a--): 先进行表达式运算，再进行自增或者自减运算
 */
public class selfAddMinus {
    public static void main(String[] args){
        int a = 3;
        System.out.println("a的值：" + a);
        System.out.println("++a的值：" + (++a));  //先计算自增（++），再进行表达式计算（=）

        int a1 = 3;
        int b1 = ++a1;
        System.out.println("a1的值：" + a1);
        System.out.println("b1的值：" + b1);

        int a2 = 3;
        System.out.println("a2的值：" + a2);
        System.out.println("a2++的值：" + a2++);  //先进行表达式计算（=），再计算自增（++）

        int a3 = 3;
        int b3 = a3++;
        System.out.println("a3的值：" + a3);
        System.out.println("b3的值：" + b3);

        int c = 3;
        System.out.println("d的值：" + c);
        System.out.println("--d的值：" + (--c));

        int c1 = 3;
        int d1 = --c1;
        System.out.println("c1的值：" + c1);
        System.out.println("d1的值：" + d1);

        int c2 = 3;
        System.out.println("c2的值：" + c2);
        System.out.println("c2--的值：" + c2--);

        int c3 = 3;
        int d3 = c3--;
        System.out.println("c3的值：" + c3);
        System.out.println("d3的值：" + d3);
    }
}
