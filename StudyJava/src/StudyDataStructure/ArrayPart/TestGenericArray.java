package StudyDataStructure.ArrayPart;

public class TestGenericArray {
    private String name;
    private int score;

    public TestGenericArray(String name, int score) {
        this.name = name;
        this.score = score;
    }

    @Override
    public String toString() {
        return String.format("Student(name:%s, score:%d)", name, score);
    }

    public static void main(String[] args) {
        GenericArray<TestGenericArray> testGenericArray = new GenericArray<>();
        testGenericArray.addLast(new TestGenericArray("test01", 66));
        testGenericArray.addLast(new TestGenericArray("test02", 77));
        testGenericArray.addLast(new TestGenericArray("test03", 88));
        System.out.println(testGenericArray);
    }
}
