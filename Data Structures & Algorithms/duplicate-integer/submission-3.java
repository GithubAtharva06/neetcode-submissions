class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
            int count = freq.getOrDefault(nums[i], 0);
            count++;
            freq.put(nums[i], count);
            if(count>1){
                return true;
            }
        }
        return false;
    }
}