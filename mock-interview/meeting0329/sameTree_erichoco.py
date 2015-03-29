# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not self.isSameNode(p, q):
            return False
        if p is None:
            return True
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameNode(self, a, b):
        if a is None or b is None:
            return a == b
        else:
            return a.val == b.val
