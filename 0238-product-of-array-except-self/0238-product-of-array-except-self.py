class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]* len(nums)
        left_prod = 1
        right_prod = 1
        for i in range (len(nums)):
            result[i]= left_prod
            left_prod *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            result[i] *= right_prod
            right_prod *= nums[i]

        return result
