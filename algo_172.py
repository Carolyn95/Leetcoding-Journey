# Factorial trailing zeros

class Solution:
    def trailingZeros(self, N):
        x = 5
        res = 0
        while x <= N:
            res += n // x
            x += 5
        return res
