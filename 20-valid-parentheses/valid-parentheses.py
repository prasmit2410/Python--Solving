class Solution:
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in pairs:
                # Check if the opening bracket matches
                if not stack or stack[-1] != pairs[char]:
                    return False

                stack.pop()

            else:
                # Opening bracket
                stack.append(char)

        # Valid only if all brackets were closed
        return len(stack) == 0