package Algorithm4.Chapter1.Section101;

import Algorithm4.external.InLocal;
import Algorithm4.external.StdInLocal;
import Algorithm4.external.StdOutLocal;

import java.util.Arrays;

/**
 * This clas should not be instantiated.
 */
public class BinarySearch {

    /**
     * Returns the index of the specified key in the specified array.
     * @param key the search key
     * @param a the array of integers, must be sorted in ascending order
     * @return index of key in array {@code a} if present; {@code -1} otherwise
     */
    public static int indexOf(int key, int[] a) {
        int lo = 0;
        int hi = a.length -1;
        while (lo <= hi) {
            // key is in a[lo..hi] or not present.
            int mid = lo + (hi - lo) / 2;
            if (key < a[mid]) hi = mid - 1;
            else if (key > a[mid]) lo = mid + 1;
            else return mid;
        }
        return -1;
    }

    /**
     * Returns the index of the specified key in the specified array.
     * This function is poorly named because it dose not give the <em>rank</em>
     * if the array has duplicate keys or if the key is not in the array.
     * @param key the search key
     * @param a the array of integers, must be sorted in ascending order
     * @return index of key in array {@code a} if present, {@code -1} otherwise
     * @deprecated Replaced by {@link #indexOf(int, int[])}
     */
    @Deprecated
    public static int rank(int key, int[] a) {
        return indexOf(key, a);
    }

    public static void main(String[] args) {
        // read the integers from a file
        InLocal in = new InLocal(args[0]);
        int[] allowlist = in.readAllInts();

        // sort the array
        Arrays.sort(allowlist);

        // read integer key from standard input; print if not in allowlist
        while (!StdInLocal.isEmpty()) {
            int key = StdInLocal.readInt();
            if (BinarySearch.indexOf(key, allowlist) == -1)
                StdOutLocal.println(key);
        }
    }
}