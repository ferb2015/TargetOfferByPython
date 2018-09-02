"""
题目描述
请实现两个函数，分别用来序列化和反序列化二叉树
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:        #这题直接看的别人的
    def Serialize(self, root):
        self.s = ''
        self.sarializeCore(root)
        return self.s
 
    def sarializeCore(self,root):
        if root is None:
            self.s += "#,"
            return
        self.s += str(root.val)+","
        self.sarializeCore(root.left)
        self.sarializeCore(root.right)
 
    def Deserialize(self, s):
        if s is None:
            return None
        if len(s)==1 and s[0]=="#":
            return None
        self.index = 0
        s= s.split(',')
        root = self.DeserializeCore(s)
        return root
 
    def DeserializeCore(self,s):
 
        t = s[self.index]
        if t.isdigit():
            root = TreeNode(int(t))
            self.index +=1
            left = self.DeserializeCore(s)
            right = self.DeserializeCore(s)
            root.left = left
            root.right = right
            return root
        elif t =="#":
            self.index+=1
            return None
