package StudyDataStructure.BSTPart;

public class TestBSTMain {
    public static void main(String[] args) {
        BST<Integer> bst = new BST<Integer>();
        int[] nums = {10,6,16,4,8,14,20,3,5,7,9};
        for (int num: nums) {
            if (num == 11) {
                System.out.println("到11了");
            }
            bst.add(num);
        }

        //二叉树结构
        //////////////////
        //      5       //
        //    /   \     //
        //   3     6    //
        //  / \     \  //
        // 2   4     8 //
        //////////////////

        System.out.println(bst);

        System.out.println("前序遍历:");
        bst.preOrder();
        System.out.println();

        System.out.println("中序遍历：");
        bst.inOrder();
        System.out.println();

        System.out.println("后序遍历：");
        bst.postOrder();
        System.out.println();

        System.out.println("层次遍历：");
        bst.levelOrder();
        System.out.println();

        System.out.println("验证2是否在二叉搜索树中：");
        System.out.println(bst.contains(2));
        System.out.println();

        System.out.println("验证不存在的10，是否在二叉搜索树中：");
        System.out.println(bst.contains(10));
        System.out.println();

        System.out.println("获取最小的元素：");
        System.out.println(bst.minimun());
        System.out.println();

        System.out.println("获取最大的元素：");
        System.out.println(bst.maximum());
        System.out.println();

//        System.out.println("删除最小的节点后的树：");
//        bst.removeMin();
//        bst.preOrder();
//        System.out.println();
//
//        System.out.println("剩余元素，删除最大的节点后的树：");
//        bst.removeMax();
//        bst.preOrder();
//        System.out.println();
//
//        System.out.println("剩余元素，删除存在的节点3：");
//        bst.remove(3);
//        bst.preOrder();
//        System.out.println();
//
//        System.out.println("剩余元素，删除不存在的节点20：");
//        bst.remove(20);
//        bst.preOrder();
//        System.out.println();

//        System.out.println("删除中间的节点3");
//        bst.remove(3);
//        bst.preOrder();
//        System.out.println();

//        System.out.println("删除中间的节点6");
//        bst.remove(6);
//        bst.preOrder();
//        System.out.println();

        int num = 6;
        System.out.println("删除指定的节点" + num);
        bst.remove(num);
        bst.preOrder();
        System.out.println();
    }
}
