# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return []
        q = deque([root])
        l = []
        ans=0
        while q:
            m = []
            for p in range(len(q)):
                node = q.popleft()
                m.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            l.append(m)
        for i in l:
            for j in i:
                if j>=low and j<=high:
                    ans+=j
        return ans