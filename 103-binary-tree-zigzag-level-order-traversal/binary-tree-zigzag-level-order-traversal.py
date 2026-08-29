# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])
        l = []
        w=1
        while q:
            m = []
            for p in range(len(q)):
                node = q.popleft()
                m.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if (w%2==0):
                m=m[::-1]
            l.append(m)
            w+=1
        return l