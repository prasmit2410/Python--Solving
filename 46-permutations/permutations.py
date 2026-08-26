class Solution:
    def permute(self, nums):
        result = []

        def backtrack(current):
            # A complete permutation is formed
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for num in nums:
                # Skip numbers already used
                if num in current:
                    continue

                current.append(num)

                # Continue building the permutation
                backtrack(current)

                # Undo the choice
                current.pop()

        backtrack([])

        return result
        