# Question : https://leetcode.com/problems/binary-tree-right-side-view/submissions/

#-----Time Complexity-----> O(n), where n is number of Node
#-----Space Complexity----> O(d), where d is the diameter of a Node


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        '''             1
                      /   \
                     2     3
                   /  \   /  \   
                  4    5 6    7     -> 4 is our Diameter for this tree
                /
               8
             Ans:- [1, 3, 7, 8]
        '''
        # Going through the code..
        # result = [1],    [1],       [1,3],     [1,3,8], [1,3,8]->This is our answer
        # level = [2, 3],  [4,5,6,7], [8],       []
        # queue = [1],     [2,3],     [4,5,6,7], []
        result = []
        level = []      # holding next level values
        queue = [root]  # current level values
        
        while queue != [] and root is not None:
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            result.append(node.val)
            queue = level
            level = []
        return result
                