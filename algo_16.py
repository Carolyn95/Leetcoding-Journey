# first unique character
import pdb
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = -1
        chars = Counter(s)
        print(chars)
        unique_chars = [char for char in chars if chars[char] == 1]
        if unique_chars:
            unique_chars_indexes = [s.index(i) for i in unique_chars]
            result = min(unique_chars_indexes)
        print(result)
        return result


if __name__ == '__main__':
    s = Solution()
    string = 'loveleetcode'
    s.firstUniqChar(string)
