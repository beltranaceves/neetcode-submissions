// import java.util.HashSet;

class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> ref = new HashSet<>();
        for (int num : nums) {
            if (ref.contains(num)) {
                return true;
            }
            ref.add(num);
        }
        return false;
    }
}