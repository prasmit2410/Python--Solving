class Solution:
    def canJump(self, nums):
        farthest = 0

        for i in range(len(nums)):
            # Current index is unreachable
            if i > farthest:
                return False

            # Update the farthest reachable index
            farthest = max(farthest, i + nums[i])

            # Last index is reachable
            if farthest >= len(nums) - 1:
                return True

        return True