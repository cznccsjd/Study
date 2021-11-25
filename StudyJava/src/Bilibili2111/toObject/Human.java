package Bilibili2111.toObject;

public class Human {
    private String name;    //变量声明成私有的
    private String sex;
    public String getName() {    //用方法来访问私有变量
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
}
