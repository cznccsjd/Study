package StudyDataStructure.StackPart;

public class TestForLeetCodeYouXiaoDeKuoHao {
    public boolean isValid(String s) {
        ArrayStack<Character> stack = new ArrayStack<Character>();

        if (s.length() % 2 == 1) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }

                char topChar = stack.pop();
                if (c == ')' && topChar == '(') {
                    return true;
                }
                if (c == ']' && topChar == '[') {
                    return true;
                }
                if (c == '}' && topChar == '{') {
                    return true;
                }
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        TestForLeetCodeYouXiaoDeKuoHao test = new TestForLeetCodeYouXiaoDeKuoHao();
        String s = "({)[}]";
        System.out.println(test.isValid(s));
    }
}
