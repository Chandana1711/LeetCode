class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        count = 1
        for i in range(1,len(nums)) :
            if nums[i] == nums[p]:
                count+=1
            else:
                count=1
            
            if count<=2:
                p+=1
                nums[p]=nums[i]
           
        return p+1