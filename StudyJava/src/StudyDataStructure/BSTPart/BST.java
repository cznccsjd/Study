package StudyDataStructure.BSTPart;

import java.util.LinkedList;
import java.util.Queue;

/**
 * 编程实现二叉搜索树
 */
public class BST<E extends Comparable<E>> {
    //定义树节点
    private class Node {
        public E e;
        public Node left, right;

        public Node(E e) {
            this.e = e;
            left = null;
            right = null;
        }
    }

    private Node root;    //根节点
    private int size;

    public BST() {
        root = null;
        size = 0;
    }

    //二分搜索树存储元素个数
    public int size() {
        return size;
    }

    //二分搜索树存储元素是否为空
    public boolean isEmpty() {
        return size == 0;
    }

    //向二分搜索树添加新的元素e
    public void add(E e) {
        root = add(root, e);
    }

    //向以node为根的二分搜索树中插入元素e
    //返回插入新节点后二分搜索树的根
    public Node add(Node node, E e) {
        //root
        if (node == null) {
            size++;
            return new Node(e);
        }

        //root的left，right分支情况
        if (e.compareTo(node.e) < 0) {  //root的left分支
            node.left = add(node.left, e);
        } else if (e.compareTo(node.e) > 0) { //root的right分支
            node.right = add(node.right, e);
        }
        return node;
    }

    //查看二分搜索树是否包含元素e（从跟节点开始）
    public boolean contains(E e) {
        return contains(root, e);
    }

    //查看以node为根的二分搜索树中是否包含元素e，递归算法
    private boolean contains(Node node, E e) {
        //递归终止条件
        if (node == null) {
            return false;
        }

        if (e.compareTo(node.e) == 0) {
            return true;
        } else if (e.compareTo(node.e) < 0) {
            return contains(node.left, e);
        } else {
            return contains(node.right, e);
        }
    }

    //二分搜索树的前序遍历（前序遍历：根节点-->左子树-->右子树）
    public void preOrder() {
        preOrder(root);
    }

    //前序遍历以node为根的二分搜索树，递归算法
    private void preOrder(Node node) {
        if (node == null) {
            return;
        }
        System.out.println(node.e);
        preOrder(node.left);
        preOrder(node.right);
    }

    //中序遍历：左子树-->根节点-->右子树
    public void inOrder() {
        inOrder(root);
    }

    //中序遍历以node为根的二分搜索树，递归算法
    private void inOrder(Node node) {
        if (node == null) {
            return;
        }
        inOrder(node.left);
        System.out.println(node.e);
        inOrder(node.right);
    }

    //后序遍历：左子树-->右子树-->根节点
    public void postOrder() {
        postOrder(root);
    }

    //后序遍历以node为根的二分搜索树，递归算法
    private void postOrder(Node node) {
        if (node == null) {
            return;
        }
        postOrder(node.left);
        postOrder(node.right);
        System.out.println(node.e);
    }

    //层次遍历（基于队列实现）
    public void levelOrder() {
        Queue<Node> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            Node cur = q.remove();
            System.out.println(cur.e);
            if (cur.left != null) {
                q.add(cur.left);
            }
            if (cur.right != null) {
                q.add(cur.right);
            }
        }
    }

    //寻找二分搜索树的最小元素
    public E minimun() {
        if (size == 0) {
            throw new IllegalArgumentException("BST is empty");
        }

        Node minNode = minimum(root);
        return minNode.e;
    }

    //返回以node为根的二分搜索树的最小值所在的节点
    private Node minimum(Node node) {
        if (node.left == null) {
            return node;
        }

        //返回相应的节点的左子树最小值
        return minimum(node.left);
    }

    //查找二分搜索树的最大元素
    public E maximum() {
        if (size == 0) {
            throw new IllegalArgumentException("BST is Empty");
        }
        Node maxNode = maximum(root);
        return maxNode.e;
    }

    //返回以Node为根的二分搜索树的最大值所在的节点
    private Node maximum(Node node) {
        if (node.right == null) {
            return node;
        }

        return maximum(node.right);
    }

    //删除最小值节点
    public E removeMin() {
        E ret = minimun();  //获取最小元素
        removeMin(root);

        return ret;
    }

    //删除以node为根的二分搜索树中的最小节点
    //返回删除节点后的新的二分搜索树的根
    private Node removeMin(Node node) {
        //递归的终止条件，当前节点没有左子树了，那就是最小节点了
        //如果是最小的节点，我们删除当前节点，但是当前节点很可能有右子树，我们先把该节点的右子树节点保存，然后删掉右子树节点，最后把右子树节点返回即可
        if (node.left == null) {
            Node rightNode = node.right;
            node.right = null;  //左节点为空了，让右子树叶微孔，相当于脱离了树
            size--;
            return rightNode;  //返回右子树是为了后面的绑定操作
        }

        node.left = removeMin(node.left);

        return node;    //擅长吧，根节点依然是Node,返回即可
    }

    //删除最大值
    public E removeMax() {
        E ret = maximum();
        removeMax(root);
        return ret;
    }

    //删除以node为根的二分搜索树中最大的节点
    //返回删除节点后新的二分搜索树的跟
    private Node removeMax(Node node) {
        if (node.right == null) {
            Node leftNode = node.left;
            node.left = null;
            size--;
            return leftNode;
        }

        node.right = removeMax(node.right);
        return node;
    }

    //从二叉搜索树中删除元素为e的节点
    public void remove(E e) {
        remove(root, e);
    }

    //删除以node为根的二叉搜索树中值为e的节点，递归算法
    //返回删除节点后更新的二叉搜索树的根
    private Node remove(Node node, E e) {
        if (node == null) {
            return null;
        }

        if (e.compareTo(node.e) < 0) {  //e<node.e 被删除的元素e小于当前节点值
            node.left = remove(node.left, e);
            return node;
        }

        if (e.compareTo(node.e) > 0) {  //e>node.e 被删除的元素e大于当前节点值
            node.right = remove(node.right, e);
            return node;
        } else {  //e == node.e，被删除的元素e等于当前节点值e
            //待删除节点左子树为空情况
            if (node.left == null) {
                Node rightNode = node.right;
                node.right = null;
                size--;
                return rightNode;
            }

            //待删除节点右子树为空情况
            if (node.right == null) {
                Node leftNode = node.left;
                node.left = null;
                size--;
                return leftNode;
            }

            //左右子树均不为空
            //方法：找到比待删除节点大的最小节点，即待删除结点右子树的最小节点
            //用这个节点顶替待删除节点的位置
            Node successor = minimum(node.right);
            successor.right = removeMin(node.right);
            successor.left = node.left;
            node.left = node.right = null;

            return successor;
        }
    }
}
