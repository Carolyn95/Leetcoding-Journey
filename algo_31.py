# 108 convert sorted array to binary search tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def make_tree(start_index, end_index):
            if start_index > end_index:
                return None
            mid_index = (start_index + end_index)//2
            this_tree_root = TreeNode(nums[mid_index])
            this_tree_root.left = make_tree(start_index,mid_index-1)
            this_tree_root.right = make_tree(mid_index+1, end_index)
            return this_tree_root
        return make_tree(0,len(nums)-1)

