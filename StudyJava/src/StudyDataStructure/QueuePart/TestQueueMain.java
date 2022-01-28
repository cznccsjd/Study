package StudyDataStructure.QueuePart;

public class TestQueueMain {
    public static void main(String[] args) {
        ArrayQueue<Integer> queue = new ArrayQueue<Integer>();
        for (int i = 0; i < 10; i++) {
            queue.enqueue(i);
            System.out.println(queue);

            if (i % 3 == 2) { //每增加3个元素出队列一个
                queue.dequeue();
                System.out.println("现在出队列一个");
                System.out.println(queue);
                System.out.println("####################");
            }
        }
    }
}