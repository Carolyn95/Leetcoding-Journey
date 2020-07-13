# plus one
import pdb
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(d) for d in digits]
        int_digits = int(''.join(digits))
        int_digits += 1
        digits = str(int_digits)
        digits = [int(d) for d in digits]
        return digits

if __name__ == "__main__":
    s = Solution()
    digits = [1, 2, 3, 4]
    s.plusOne()
