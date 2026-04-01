# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #can technically recurse in any order, but will prob do preorder
        #should follow a normal traversal because if equivalent, should traverse in the same way, just add logic for equivalency

        #implement the base case, if both are null, if one is null/other isn't, if mismatch in node values

        if p == None and q == None:
            return True
        if p == None and q != None:
            return False
        if p != None and q == None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        #self.isSameTree(p.right, q.right)
        #return True