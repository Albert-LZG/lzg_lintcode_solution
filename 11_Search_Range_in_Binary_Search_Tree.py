"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        # write your code here
        result = []
        if root:
            if root.val >= k1 and root.val <= k2:
                result.append(root.val)
                result.extend(self.searchRange(root.left, k1, k2))
                result.extend(self.searchRange(root.right, k1, k2))
            elif root.val < k1:
                result.extend(self.searchRange(root.right, k1, k2))
            else:
                result.extend(self.searchRange(root.left, k1, k2))
        result.sort()
        return result