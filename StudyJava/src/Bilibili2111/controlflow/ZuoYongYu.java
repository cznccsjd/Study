package Bilibili2111.controlflow;

public class ZuoYongYu {
    public void method() {
        int n;
        {
            int k;
//            n++;    //该语句合法
        }
//        k++;  //该语句非法
    }
}
