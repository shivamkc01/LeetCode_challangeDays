# Question link -> https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
                        1
                     /     \
                   2         3
                /    \      /  \
               4     5     6    7
        
root = [1,2,3,4,5,6,7]
result will be = [[1], [2,3], [4,5,6,7]]

queue = [1]->[2,3] ->[4,5,6,7] -> [4,5,6,7]->[]
level = [1]->[2,3] -> [] -> [4,5,6,7]->[]
next_queue = [2,3]->[]->[4,5,6,7]-> []->[4,5,6,7]->[]
result = [[1], [2,3], [4,5,6,7]]

Our final result for this tree will be:
result = [[1], [2,3], [4,5,6,7]]
return result
'''

# Time Complexity -----> O(nm), where n is depth
# Space Complexity ----> O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = [root]
        level = []
        next_queue = []
        result = []
        
        
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
        return result
       
                
                
                
                
                
        