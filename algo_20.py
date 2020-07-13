# 125 valid palindrome
import pdb
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^\w\s]','',s)
        s = ''.join([e.lower() for e in s.split() if e.isalnum()])
        l, r = 0, len(s)
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    string = "A man, a plan, a canal: Panama"
    s.isPalindrome(string)
