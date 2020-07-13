# rotate array
import pdb


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        swap(0, n - k - 1)
        swap(n - k, n - 1)
        swap(0, n - 1)


if __name__ == "__main__":
    s = Solution()
    # nums = [-1, -100, 3, 99] # 2
    nums = [1, 2, 3, 4, 5, 6, 7]  # 3
    # nums = [1, 2]  # 3
    k = 3  # 2
    s.rotate(nums, k)
    """Sol-1
    class Solution:
    def rotate(self, nums, k):
        # Do not return anything, modify nums in-place instead.

        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]
    """