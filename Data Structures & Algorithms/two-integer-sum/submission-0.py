class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenbefore = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seenbefore:
                return [seenbefore[needed], i]
            seenbefore[nums[i]] = i