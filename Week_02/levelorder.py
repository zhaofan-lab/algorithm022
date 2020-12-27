class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []

        result = []
        queue = [root]
        while queue:
            n = len(queue)
            children = []
            for i in range(0, n):
                temp = queue.pop(0)
                children.append(temp.val)
                if temp.children:
                    queue.extend(temp.children)
            result.append(children)
        return result
