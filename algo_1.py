# Two sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution1:

  def twoSum(self, nums, target):
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
          return [i, j]


# Optimised using hash map
class Solution:

  def twoSum(self, nums, target):
    hash_map = {}
    for i, n in enumerate(nums):
      remaining = target - n
      if remaining in hash_map:
        return [i, hash_map[remaining]]
      else:
        hash_map[n] = i


if __name__ == '__main__':
  nums = [2, 7, 11, 15]
  target = 9
  sol = Solution()
  res = sol.twoSum(nums, target)
  print(res)