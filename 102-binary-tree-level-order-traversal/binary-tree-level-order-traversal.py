class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=deque([root])
        l=[]
        while q:
            m=[]
            for _ in range(len(q)):
                node=q.popleft()
                m.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            l.append(m)
        return l

        