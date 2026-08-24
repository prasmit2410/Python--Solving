class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    # Start a new possible substring
                    stack.append(i)
                else:
                    # Calculate the valid substring length
                    max_len = max(max_len, i - stack[-1])

        return max_len