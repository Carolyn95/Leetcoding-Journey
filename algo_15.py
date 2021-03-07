# ThreeSum
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Notice that the solution set must not contain duplicate triplets.


class Solution1:

  # brute force
  def threeSum(self, nums):
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


class Solution2:
  # optimized brute force
  def threeSum(self, nums):
    nums.sort()
    N = len(nums)
    res = []
    for i in range(N):
      for j in range(i + 1, N):
        for k in range(j + 1, N):
          ans = [nums[i], nums[j], nums[k]]
          if sum(ans) == 0 and ans not in res:  # optimize solution1 here
            res.append(ans)

    return res


class Solution3:
  # double pointer
  def threeSum(self, nums):
    res = []
    N = len(nums)
    if N < 3:
      return res

    nums.sort()
    for i in range(N - 2):
      j = i + 1
      k = N - 1
      while j < k:
        temp = [nums[i], nums[j], nums[k]]
        added = sum(temp)
        if added > 0:
          k -= 1
        else:
          j += 1
        if temp not in res and added == 0:
          res.append(temp)

    return res


class Solution:
  # optimized double pointer
  def threeSum(self, nums):
    res = []
    N = len(nums)
    if N < 3:
      return res

    nums.sort()
    for i in range(N - 2):
      j = i + 1
      k = N - 1
      while j < k:
        temp = [nums[i], nums[j], nums[k]]
        added = sum(temp)
        if added > 0:
          k -= 1
        elif added < 0:
          j += 1
        else:
          j += 1
          if res:
            if temp not in res:
              res.append(temp)
          else:
            res.append(temp)

    return res


if __name__ == '__main__':
  nums = [-1, 0, 1, 2, -1, -4]
  ans = [[-1, -1, 2], [-1, 0, 1]]
  sol = Solution()
  res = sol.threeSum(nums)
  print(res)
