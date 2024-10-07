class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        result = []
    
        for i in range(len(nums) - 2):
        # Skip the same `nums[i]` to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
        # Initialize two pointers
            left, right = i + 1, len(nums) - 1
        
            while left < right:
                total = nums[i] + nums[left] + nums[right]
            
                if total == 0:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])
                
                    # Move left and right to the next different numbers to avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                
                    # Move both pointers after processing a valid triplet
                    left += 1
                    right -= 1
            
                elif total < 0:
                    left += 1  # We need a larger sum
                else:
                    right -= 1  # We need a smaller sum
                
        return result
        
        
        
