# Problem: https://leetcode.com/problems/merge-two-binary-trees/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if self.left is None:
                self.left = TreeNode(val)
                return
            elif self.left.val is not 'null':
                self.left.insert(val)
                return

            if self.right is None:
                self.right = TreeNode(val)
            elif self.right.val is not 'null':
                self.right.insert(val)
        else:
            self.val = val

    def print_tree(self):
        array = []
        self.tree_to_array(array)
        print(array)

    def tree_to_array(self, array):
        array.append(self.val)

        if self.left:
            self.left.tree_to_array(array)

        if self.right:
            self.right.tree_to_array(array)


# Solution start
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2

        if t2 is None:
            return t1

        # For local test
        t1.val += t2.val if t2.val is not 'null' else 0

        # Works on LeetCode
        # t1.val += t2.val

        if t1.left and t2.left:
            t1.left = self.mergeTrees(t1.left, t2.left)

        if t1.left is None:
            t1.left = t2.left

        if t1.right and t2.right:
            t1.right = self.mergeTrees(t1.right, t2.right)

        if t1.right is None:
            t1.right = t2.right

        return t1


# Generate two trees
t1 = [1, 3, 2, 5]
t2 = [2, 1, 3, 'null', 4, 'null', 7]

t1_root = TreeNode(t1[0])
for i in range(1, len(t1)):
    t1_root.insert(t1[i])

t2_root = TreeNode(t2[0])
for i in range(1, len(t2)):
    t2_root.insert(t2[i])

print('***Tree 1***')
t1_root.print_tree()
print('***Tree 2***')
t2_root.print_tree()

# Output
solution = Solution()
output = solution.mergeTrees(t1_root, t2_root)
print('***Output***')
output.print_tree()
