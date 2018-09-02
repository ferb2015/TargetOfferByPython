"""
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""
# 这题比上面那题简单一些，基本上就是这题的变形就是上面那题之字型打印

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
            if not pRoot:
                return []
            level, result, lefttoright = [pRoot], [], True
            while level :
                nextlevel ,curres = [], []
                for node in level:
                    curres.append(node.val)
                    if node.left:
                        nextlevel.append(node.left)
                    if node.right:
                        nextlevel.append(node.right)
                if not lefttoright:
                    curres.reverse()
                #lefttoright = not lefttoright
                if curres:
                    result.append(curres)
                level = nextlevel
            return result
