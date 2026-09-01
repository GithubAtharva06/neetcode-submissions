class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            count = freq.get(nums[i], 0) + 1
            freq[nums[i]] = count
            if count >  len(nums) // 2:
                return nums[i]
        