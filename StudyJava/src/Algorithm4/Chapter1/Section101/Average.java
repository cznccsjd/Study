package Algorithm4.Chapter1.Section101;

import Algorithm4.external.StdInLocal;
import Algorithm4.external.StdOutLocal;

public class Average {
    public static void main(String[] args) {
        // 取StdIn中所有数的平均值
        double sum = 0.0;
        int cnt = 0;
        while (!StdInLocal.isEmpty()) {
            // 读取一个数并计算累计之和
            sum += StdInLocal.readDouble();
            cnt++;
        }
        double avg = sum / cnt;
        StdOutLocal.printf("Average is %.5f\n", avg);
    }
}
