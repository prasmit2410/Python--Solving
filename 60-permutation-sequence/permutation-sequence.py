class Solution:
    def getPermutation(self, n, k):
        numbers = [str(i) for i in range(1, n + 1)]
        result = []

        # Convert k to 0-based indexing
        k -= 1

        # Factorials
        factorial = 1
        for i in range(1, n):
            factorial *= i

        for i in range(n, 0, -1):
            # Find which block k belongs to
            index = k // factorial

            result.append(numbers[index])
            numbers.pop(index)

            # Update k for the next position
            k %= factorial

            if i > 1:
                factorial //= (i - 1)

        return ''.join(result)