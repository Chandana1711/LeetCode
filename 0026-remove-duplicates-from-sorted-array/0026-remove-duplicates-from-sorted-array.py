class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = list(set(nums))
        # return len(nums)
        p = 0
        
        for i in range(1,len(nums)):
            if nums[i] != nums[p]:
                p += 1
                nums[p] = nums[i]
                
        return p+1
                
