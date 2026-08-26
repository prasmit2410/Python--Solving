class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        # Maximum possible number of digits
        result = [0] * (m + n)

        # Multiply each digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2

                position = i + j + 1
                carry_position = i + j

                total = product + result[position]

                result[position] = total % 10
                result[carry_position] += total // 10

        # Remove leading zeros
        start = 0

        while start < len(result) and result[start] == 0:
            start += 1

        return ''.join(map(str, result[start:]))