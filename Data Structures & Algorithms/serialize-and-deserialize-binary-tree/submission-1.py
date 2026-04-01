# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        #use depth first search pre order to go through the 
        s = ""

        def dfs(root):
            nonlocal s
            if not root:
                s += "N,"
                return
            s += str(root.val) + ","

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        print(s)
        return s

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #break the data into a binary tree, we start at the root

        vals = data.split(",")

        i = 0

        def dfs():
            nonlocal i

            if vals[i] == "N":
                i += 1
                return None
            
            node = TreeNode(int(vals[i]))
            i += 1

            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()



