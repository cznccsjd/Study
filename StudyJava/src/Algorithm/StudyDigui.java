package Algorithm;

/**
 * 熟悉递归
 * 学习链接：https://www.zhihu.com/question/31412436
 */

public class StudyDigui {
    /**
     * 递归三要素：
     * 1、明白你这个函数想要干什么；
     * 2、寻找递归结束条件；
     * 3、找出函数的等价关系式
     */
    //定义一个阶乘函数 （假设n不为0）
    int f(int n) {
        if (n <= 2) {
            return n;
        }

        //把f(n)的等价操作写进去
        return f(n-1) * n;
    }

    //案例1：斐波那契数列
    int fib(int n) {
        //1.先写出递归结束条件
        if (n <= 2) {
            return 1;
        }
        //2.接着写等价关系式
        return f(n-1) + f(n-2);
    }

    //案例2：小青蛙跳台阶,一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
    int frog(int n) {
        if (n <= 2) {
            return 2;
        }
        return f(n-1) + f(n-2);
    }

    //案例3：反转单链表
    public static Node reverseList(Node head) {
        //1.递归结束条件
        if (head == null || head.next == null) {
            return head;
        }
        //递归反转子链表
        Node newList = reverseList(head.next);
        //改变1，2节点的指向
        //通过head.next获取节点2
        Node t1 = head.next;
        //让2的next指向2
        t1.next = head;
        //1的next指向null
        head.next = null;
        //返回调整后的链表
        return newList;
    }

    //递归优化，去除重复计算的部分
    int Newf(int n) {
        Integer arr[] = new Integer[0];
        if (n <= 1) {
            return n;
        }
        //先判断有没有计算过
        if (arr[n] != -1) {
            //计算过，直接返回
            return arr[n];
        } else {
            //没有计算过，递归计算，并且把结果保存到arr数组中
            arr[n] = Newf(n-1) + Newf(n-1);
            return arr[n];
        }
    }

    //递归优化，自底向上计算，也叫做递推
    public int upf(int n) {
        if (n <= 2) {
            return n;
        }
        int upf1 = 1;
        int upf2 = 2;
        int sum = 0;

        for (int i = 3; i <= n; i++) {
            sum = upf1 + upf2;
            upf1 = upf2;
            upf2 = sum;
        }
        return sum;
    }
}

class Node<E> {
    E val;
    Node next;
    Node() {
        this.val = null;
        this.next = null;
    }

    Node(E val) {
        this.val = val;
        this.next = null;
    }

    Node(E val, Node next) {
        this.val = val;
        this.next = next;
    }
}