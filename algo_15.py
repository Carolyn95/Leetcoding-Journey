# ThreeSum
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Notice that the solution set must not contain duplicate triplets.


class Solution:

  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    N = len(nums)
    res = []
    for i in range(N):
      for j in range(i + 1, N):
        for k in range(j + 1, N):
          if nums[i] + nums[j] == -nums[k]:
            res.append([nums[i], nums[j], nums[k]])
    real_res = [r for i, r in enumerate(res) if r not in res[i + 1:]]

    return real_res


if __name__ == '__main__':
  nums = [-1, 0, 1, 2, -1, -4]
  ans = [[-1, -1, 2], [-1, 0, 1]]
  sol = Solution()
  res = sol.threeSum(nums)
  print(res)
