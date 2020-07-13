# contains duplicates
# returns true if contains duplicates else false
class Solution:
    def containsDuplicate(self, nums):
        return False if len(nums) == len(set(nums)) else True

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for n in nums:
            if n not in hash_map:
                hash_map[n] = 1
            else:
                return True
        if len(hash_map) == len(nums):
            return False

