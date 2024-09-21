class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reachable = 0
        jump_count = 0
        curr_end = 0
        for i in range(0, len(nums)-1):
            max_reachable = max(max_reachable, i+nums[i])

            if i == curr_end:
                jump_count += 1
                curr_end = max_reachable
            
            if curr_end >= len(nums)-1:
                break

        return jump_count