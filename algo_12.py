# remove duplicates from sorted arrays
class Solution:
    def removeDuplicates(self, nums):
        length = len(nums)
        for i in range(length - 1, 0, -1):
            j = i - 1
            if nums[i] == nums[j]:
                nums.pop(i)
        print(len(nums))
        return len(nums)




if __name__ == "__main__":
    s = Solution()
    # nums = [1,1,2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    s.removeDuplicates(nums)
    """
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.remove(nums[i])
                continue
            else:
                i = j
            j += 1
        print(nums)
    """
