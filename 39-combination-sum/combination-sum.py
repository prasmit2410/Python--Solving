class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, total):
            # Target reached
            if total == target:
                result.append(current.copy())
                return

            # Sum exceeded
            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                # Use the same number again
                backtrack(i, current, total + candidates[i])

                # Undo the choice
                current.pop()

        backtrack(0, [], 0)

        return result
        