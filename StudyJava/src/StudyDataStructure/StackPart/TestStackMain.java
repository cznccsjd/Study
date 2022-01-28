package StudyDataStructure.StackPart;

public class TestStackMain {
    public static void main(String[] args) {
        ArrayStack<Integer> stack = new ArrayStack<Integer>();

        //测试进栈操作
        System.out.println("测试进栈：");
        for (int i = 0; i < 5; i++) {
            stack.push(i);
            System.out.println(stack);
        }
        System.out.println("查看当前的栈顶元素：" + stack.peek());

        //测试出栈操作
        System.out.println("测试出栈");
        stack.pop();
        System.out.println(stack);
        System.out.println("查看当前的栈顶元素:" + stack.peek());
    }
}
