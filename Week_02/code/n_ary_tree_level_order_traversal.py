"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        res = collections.defaultdict(list)
        self.dfs(root, 0, res)
        return [res[height] for height in range(max(res) + 1)]
        
    def dfs(self, root: 'Node', height: int, res: List[List[int]]):
        if root:
            res[height].append(root.val)
            for child in root.children:
                if child:
                    self.dfs(child, height + 1, res)
