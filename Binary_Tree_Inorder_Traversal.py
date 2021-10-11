# Question link ->  https://leetcode.com/problems/binary-tree-inorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''----------------------------------------------------------
                        1
                     /     \
                    2       3
                 /    \    /  \ 
                4      5  6     7
              / 
             8


# [1,2,3,4,5,6,7,8,9]
# root = [1] -> [2] -> [4]->[8]->None->[8] 
# Stack = [1]-> [1, 2] -> [1,2,4], [1,2,4,8]->[1,2,4]->[1, 2]->[1]
# result = [8] -> [8,4] -> [8, 4, 2] -> [8, 4,2 ,5]-> [8, 4, 2,5, 1]
->[8,4,2,5,1,6,3,7]
final answer result = [8,4,2,5,1,6,3,7]
return result
-----------------------------------------------------------'''

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ Method I using recrusive"""
        # Time Complexity ----> O(nm), where n is the depth, m is no of iteration
        # Space Complexity ---> O(m) 
        if root is None:
            return []    
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

#---------------------------------------------------------------------------------#

        """ Method II - USING STACK FIFO METHOD"""
        # Time Complexity -----> O(n)
        # Space Complexity ----> O(n)
        stack = []
        result = []
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
            
    
        
        