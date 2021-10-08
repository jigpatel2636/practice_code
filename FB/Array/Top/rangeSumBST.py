'''
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
'''


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.total = 0

        def inorder(root):
             if root:
                 if root.val > low :
                     inorder(root.left)
                 if low <= root.val <= high:
                     self.total += root.val
                 if root.val < high:
                     inorder(root.right)

        inorder()
        return self.total

