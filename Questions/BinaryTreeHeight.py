"""
TreeNode
    int val;
    TreeNode left;
    TreeNode right;
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        """
              |
            |   |
          |  |    |
        |
        """


# https://leetcode.com/problems/maximum-depth-of-binary-tree/

def find_depth(root: TreeNode) -> int:
    if root == None:
        return 0
    final_depth_left = find_depth(root.left)
    final_depth_right = find_depth(root.right)
    final_depth = max(final_depth_left, final_depth_right)

    return final_depth + 1
