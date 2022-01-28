package StudyDataStructure.StackPart;

public class TestLinkedListStackMain {
    public static void main(String[] args) {
        LinkedListStack<Integer> stack = new LinkedListStack<Integer>();
        for (int i = 0; i < 5; i++) {
            stack.push(i);
            System.out.println(stack);
        }
        System.out.println("出栈一个元素：");
        stack.pop();
        System.out.println(stack);
        System.out.println("#############################");
    }
}
