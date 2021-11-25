package Bilibili2111.toObject;

public class Children extends Parent{
    public void print() {
        System.out.println(pString);
    }

    public static void main(String[] args){
        Children child = new Children();
        child.print();
    }
}
