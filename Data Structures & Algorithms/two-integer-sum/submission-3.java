class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> ref = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            int diff = target - current;
            if (ref.containsKey(diff)) {
                return (new int[]{ref.get(diff), i});
            } else {
                ref.put(current, i);
            }
        }
        return (new int[]{});
    }
}
