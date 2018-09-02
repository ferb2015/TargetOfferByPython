"""
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""
#中序遍历 dfs

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k == 0:
            return 
        if not pRoot:
            return 
        res = []
        def dfs(pRoot):
            if not pRoot:
                return
            dfs(pRoot.left)
            res.append(pRoot)
            dfs(pRoot.right)
        dfs(pRoot)
        if k>len(res):
            return 
        return res[k-1]
