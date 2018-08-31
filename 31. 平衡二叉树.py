"""
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""

# 看的牛客网其他人的回答。

# 方法一：自顶向下,对于每个节点，都计算一下左子树以及右子树的深度差的绝对值，即每个节点都判断一下。（借鉴了上一题） 算法复杂度为O（N*2）

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, p):
        if p is None:
            return True
        left = self.depth(p.left)
        right = self.depth(p.right)
        return abs(left - right) <=1 and self.IsBalanced_Solution(p.left) and self.IsBalanced_Solution(p.right)
    def depth(self, p):
        if p is None:
            return 0
        return 1 + max(self.depth(p.left), self.depth(p.right))
        
# 方法二：自下往上 算法复杂度O(N)

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, p):
        return self.dfs(p) != -1
    def dfs(self, p):
        if p is None:
            return 0
        left = self.dfs(p.left)
        if left == -1:
            return -1
        right = self.dfs(p.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
