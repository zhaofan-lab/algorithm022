#解法一：递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        result = []
        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)

        return result

#解法二：颜色标记法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

#解法三：栈迭代
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result