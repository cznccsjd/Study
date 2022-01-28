package StudyDataStructure.RecursionPart;

/**
 * 使用虚拟头节点
 * Bug啊，完全没看懂作者在干嘛
 */
//public class Solution3 {
//    public ListNodeForSolution3 removeElement(ListNodeForSolution3 head, int val) {
//        if (head == null) {
//            return null;
//        }
//
//        ListNodeForSolution3 res = removeElement(head.next, val);
//
////        if (head.e == val) {
////            return res;
////        }
////    }
//}

class ListNodeForSolution3<E> {
     public E e;
     public ListNodeForSolution3 next;

     ListNodeForSolution3(E e, ListNodeForSolution3 next) {
         this.e = e;
         this.next = next;
     }

     ListNodeForSolution3(E e) {
         this.e = e;
         this.next = null;
     }

     ListNodeForSolution3() {
         this.e = null;
         this.next = null;
     }
}
