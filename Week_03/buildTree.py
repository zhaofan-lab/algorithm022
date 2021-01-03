# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        length = len(preorder)
        if length == 0:
            return None

        root = TreeNode(preorder[0])
        inloc = 0
        for i in range(0, length):
            if preorder[0] == inorder[i]:
                inloc = i
                break
        root.left = self.buildTree(preorder[1:inloc+1], inorder[0:inloc])
        root.right = self.buildTree(preorder[inloc+1:], inorder[inloc+1:])

        return root
