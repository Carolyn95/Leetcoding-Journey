# 102 binary tree level order traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        nodes = [(root,)]
        values = []
        while nodes:
            values.append([r.val for n in nodes for r in n if r])
            nodes = [(r.left, r.right) for n in nodes for r in n if r]
        return values[:-1]

