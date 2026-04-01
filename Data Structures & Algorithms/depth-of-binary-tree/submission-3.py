# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #stack is initialized to whatever the root is and 1
        stack = [[root, 1]]

        #our result is 0 because we dont track any depth yet
        res = 0

        #loop will go through entire stack
        while stack:
            #the node as well as the depth is captured, removed from stack
            node, depth = stack.pop()

            #handles null nodes and base case by ignoring it
            if node:
                #if the depth is bigger, it becomes res
                res = max(res, depth)
                #tracks nodes to left and right of root as well as their depth position
                stack.append([node.left, depth +1])
                stack.append([node.right, depth +1])
        return res



