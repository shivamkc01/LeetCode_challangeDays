# Question link -> https://leetcode.com/problems/binary-tree-preorder-traversal/


# Definition for a binary tree node.
# It is good to remember that pre-order traversal traverses a tree in the order of # root->left->right.
'''
pre-order follow = [root->left->right]
but I did = [root->right->left]
                        1
                     /     \
                   2         3
                /    \      /  \
               4     5     6    7
             /
            8
            
[1,2,4,8,5,3,6,7]


stack  = [1] ->[ ]->[3,2]->[3,5,4]->[3,5,8]->[3,5]->[3]->[7,6]->[7]->[]
result = []  ->[1]->[1,2]->[1,2,4]->[1,2,4,8]->[1,2,4,8,5]->[1,2,4,8,5,3]->[1,2,4,8,5,3,6]----Ans-[1,2,4,8,5,3,6,7]
root   = []  ->[1]->[2  ]->[4]    ->[8]->[5]->[3]->[6]->[7]->[]
final result = [1,2,4,8,5,3,6,7]
return result
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ Using Recrusion Method """
        # Time Complexity ----> O(nm), where n is the depth & m is the no of calling to the function.
        # Space Complexity ---> O(m)
        # if root is None:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        
        """ Using iterative Method """
        # Time Complexity -----> O(n)
        # Space Complexity ----> O(n)
        stack = [root]
        result = []
        while stack != []:
            root = stack.pop()
            result.append(root.val)
            if root.right is not None:   # first we are pushing right val -> []
                stack.append(root.right)
            if root.left is not None:    # and then we are pushing left val
                stack.append(root.left)
        return result
        
            
                
    