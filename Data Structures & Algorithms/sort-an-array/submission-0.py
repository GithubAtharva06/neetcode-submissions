class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums, 0, len(nums) - 1)
        return nums

    def mergesort(self, nums: List[int], low, high): 
        if(low>=high): 
            return 
        mid = (low + high) // 2 
        self.mergesort(nums, low, mid) 
        self.mergesort(nums, mid + 1, high) 
        self.merge(nums, low, mid, high)

    def merge(self, nums, low, mid, high):
        i = low
        j = mid + 1
        temp = []
        while i<= mid and j<= high:
            if nums[i]< nums[j]:
                temp.append(nums[i])
                i = i+1
            else:
                temp.append(nums[j])
                j = j + 1
        while i<= mid:
            temp.append(nums[i])
            i = i+1
        while j<= high:
            temp.append(nums[j])
            j = j+1
        for k in range(len(temp)):
            nums[low + k] = temp[k]

        return nums

