class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p=0     #pointer
        i=0     #iterator
        while i < len(nums):
            if nums[i] != val:
                nums[p]= nums[i]           
                p +=1
            i +=1
        return p