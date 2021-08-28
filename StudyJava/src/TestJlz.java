public class TestJlz {
    public static void main(String[] args){
        double[] myList = {1.1, 2.1, 3.1, 4,1, 5,1, 6,1, 7.1};
        System.out.println(myList);
        int n = myList.length;
        double sum = 0.0;
        for(int i = 0; i < n; i++){
            double tmp = myList[i];
            myList[i] = myList[n-i-1];
            myList[n-i-1] = tmp;
        }
        System.out.println(myList);
    }
}
