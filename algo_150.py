# move zeros
import pdb
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length - 2, -1, -1):
            print(i)
            if nums[i] == 0:
                nums.append(0)
                nums.pop(i)

        print(nums)

if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
