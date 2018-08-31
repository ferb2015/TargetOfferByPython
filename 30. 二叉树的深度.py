"""
题目描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""

# 这题看了剑指 offer的讲解，太巧妙了，哎，自己写不出来。 我一直在考虑的都是只有左子树或只有右子树时，深度加1。 
# 没考虑到左右子树都有的时候，要考虑二者的深度大小对比了，二者都有的情况下，左深度大于右边深度，深度为左子树+1！反之亦然。

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        nl = self.TreeDepth(pRoot.left)
        nr = self.TreeDepth(pRoot.right)
        if nl > nr:
            return nl+1
        else:
            return nr+1
# 或者直接写成：

def maxDepth(p):
        if not p:
            return 0
        return 1 + max(maxDepth(p.left),maxDepth(p.right))
