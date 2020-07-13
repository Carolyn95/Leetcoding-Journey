# 14 longest common prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        zipped_strs = zip(*strs)
        for i in zipped_strs:
            if len(set(i)) == 1:
                res += i[0]
            else:
                break
        return res
