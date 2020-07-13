# 28 implement strStr
import pdb
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        window = len(needle)
        result = -1
        i = 0
        while i <= len(haystack) - window:
            print(i)
            print(haystack[i:i+window])
            if haystack[i: i+window] == needle:
                result = i
                break
            i += 1
        print(result)
        return result

if __name__ == '__main__':
    s = Solution()
    #haystack = "aaaaa"
    haystack = "mississippi"
    needle = "pi"
    s.strStr(haystack, needle)
