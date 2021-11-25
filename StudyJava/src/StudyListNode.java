class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x;}
}
public class StudyListNode {
    public static void main(String[] args) {
        ListNode head = new ListNode(0);
        ListNode firstNode = new ListNode(1);
        ListNode secondNode = new ListNode(2);
        ListNode thirdNode = new ListNode(3);
        head.val = 1;
        head.next = firstNode;
        firstNode.next = secondNode;
        secondNode.next = thirdNode;
        a(head);
    }

    public static void a(ListNode ll) {
        System.out.println("secondNode的值为：" + ll.next.next.val);
        System.out.println("head的值：" + ll.val);
    }

    public static ListNode add(ListNode l1, ListNode l2) {
        /*
        给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
        如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
        您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
        示例：
            输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
            输出：7 -> 0 -> 8
            原因：342 + 465 = 807
        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/add-two-numbers
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        ————————————————
        版权声明：本文为CSDN博主「潇雪凌宇」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
        原文链接：https://blog.csdn.net/weixin_44407699/article/details/97612537

        我们先来分析一下这道题
        要在每次计算后，跳到下一个节点
        产生进位怎么运算
        两个链表长度不同，我们应该怎么处理
        如果最高位相加正好等于10，怎么处理
        我们都可以通过if()条件语句来设置条件解决

        下面是我的解法，可供参考，逻辑基本上都是较为简单的，代价就是代码量稍微大了点
         */
        ListNode result = new ListNode(0);    //接收结果
        ListNode l1flag = l1;    //为了方便计算确保l1 l2 result的结构不受变化，建立flag
        ListNode l2flag = l2;
        ListNode resultflag = new ListNode(0);
        resultflag = result;
        int num = 0;   //存储进位
        while (l1flag != null) { //l1flag存在
            if(l2flag == null) {    //l1flag不为空，l2flag为空
                resultflag.val = l1flag.val + num;
                num = 0;
                if (resultflag.val >= 10) {
                    num = 1;
                    resultflag.val -= 10;
                }
                l1flag = l1flag.next;    //flag指向下一个节点
                if(l1flag != null || num != 0) {
                    resultflag.next = new ListNode(0);
                    resultflag = resultflag.next;
                }
            }

            if (l2flag != null){//都不为空的情况
                resultflag.val = l1flag.val + l2flag.val + num;
                if (resultflag.val >= 10) {
                    num = 1;
                    resultflag.val -= 10;
                }else{
                    num = 0;
                }
                l1flag = l1flag.next;
                l2flag = l2flag.next;
                if(l2flag != null || l1flag != null || num != 0){
                    resultflag.next = new ListNode(0);
                    resultflag = resultflag.next;
                }
            }

        }
        while (l2flag != null) {//这里有Bug，至少覆盖的不全
            resultflag.val = l2flag.val + num;
            num = 0;
            if(resultflag.val >= 10) {
                num = 1;
                resultflag.val -= 10;
            }
            l2flag = l2flag.next;
            if(l2flag != null || num != 0) {
                resultflag.next = new ListNode(0);
                resultflag = resultflag.next;
            }
        }
        if(l1flag == null && l2flag == null && num != 0) {//最高位相加正好为10产生进位
            resultflag.val = num;
            num = 0;
        }
        return result;
    }
}
