# 53 maximum subarray
class Solution:
    def maxSubArray(self, nums):
        results = []
        if len(nums) == 1:
            return nums[0]
        for i, n in enumerate(nums):
            if results == []:
                result = n
            else:
                result = max(results[i - 1] + n, n)
            results.append(result)
        print(results)
        print(max(results))
        return max(results)


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s.maxSubArray(nums)
