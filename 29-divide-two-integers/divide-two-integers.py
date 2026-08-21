class Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Special overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Subtract the largest possible multiples of divisor
        while dividend >= divisor:
            value = divisor
            multiple = 1

            while dividend >= (value << 1):
                value <<= 1
                multiple <<= 1

            dividend -= value
            quotient += multiple

        # Apply the sign
        if negative:
            quotient = -quotient

        # Clamp to 32-bit signed integer range
        if quotient > INT_MAX:
            return INT_MAX

        if quotient < INT_MIN:
            return INT_MIN

        return quotient