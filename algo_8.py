# 136 single number - array
from collections import Counter


class Solution:
    def singleNumber(self, nums):
        freq_count = Counter(nums)
        for key in freq_count:
            if freq_count[key] == 1:
                return key


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         unique_nums = list(set(nums))
#         return 2 * sum(unique_nums) - sum(nums)

if __name__ == "__main__":
    s = Solution()
    nums = [4, 1, 2, 1, 2]  # [2, 2, 1]
    s.singleNumber(nums)