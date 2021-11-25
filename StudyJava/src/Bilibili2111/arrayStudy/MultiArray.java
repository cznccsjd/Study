package Bilibili2111.arrayStudy;

public class MultiArray {
    public static void main(String[] args){
        Object[][] object = new Object[3][5];
        object[0][0] = 1;
        object[0][1] = "张三";
        object[0][2] = "女";
        object[0][3] = 88;
        object[0][4] = 95;
        object[1][0] = 2;
        object[1][1] = "李四";
        object[1][2] = "男";
        object[1][3] = 72;
        object[1][4] = 68;
        object[2][0] = 3;
        object[2][1] = "王五";
        object[2][2] = "女";
        object[2][3] = 68;
        object[2][4] = 85;

        for(int i=0;i<object.length;i++){
            for(int j=0;j<object[i].length;j++){
                System.out.println("object["+i+"]["+j+"]="+object[i][j]);
            }
        }
    }
}
