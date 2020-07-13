# twoSum
import pdb


class Solution:
    def twoSum(self, nums, target):
        # one solution, return indexes from original array which two elements can add up to target
        hash_map = {}
        for i, n in enumerate(nums):
            target_value = target - n
            if target_value in hash_map:
                print([hash_map[target_value], i])
                return [hash_map[target_value], i]
            hash_map[n] = i


if __name__ == "__main__":
    s = Solution()
    target = 9
    nums = [2, 7, 11, 15]
    # nums = [3, 2, 4]
    s.twoSum(nums, target)
"""Sol_1
class Solution:
    def twoSum(self, nums, target):
        # one solution, return indexes from original array which two elements can add up to target
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(i, j)
                    return [i, j]

if __name__ == "__main__":
    s = Solution()
    target = 6
    # nums = [2, 7, 11, 15]
    nums = [3,2,4]
    s.twoSum(nums, target)
"""