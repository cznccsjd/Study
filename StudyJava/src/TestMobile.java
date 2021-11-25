public class TestMobile {
    public static String mobileNumber(String mobile){
//        手机的位数是11位，java中int的长度是10位，所以得用long
//        int m = Integer.parseInt(mobile);
//        int n = m - 1;
        long m = Long.parseLong(mobile);
        long n = m - 1;
        return String.valueOf(n);
    }

    public static void main(String[] args){
        String in = "19029991234";
        String m = mobileNumber(in);
        System.out.println(m);
    }
}