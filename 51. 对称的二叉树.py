"""
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""
# 重点在于新建的'#'结点，这个想得比较久。

class Solution:
    def isSymmetrical(self, pRoot): #中序遍历 以根节点为中心，对称
        # write code here
        a = []
        def zhongxu(pRoot):
            if not pRoot:
                #newNode = TreeNode('#')
                #a.append(newNode.val)
                return
            if pRoot.left and not pRoot.right:
                pRoot.right = TreeNode('#')
            elif pRoot.right and not pRoot.left:
                pRoot.left = TreeNode('#')
            zhongxu(pRoot.left)
            a.append(pRoot.val)
            zhongxu(pRoot.right)
        zhongxu(pRoot)
        lens = len(a)
        for i in range(lens>>1):
            if a[i] != a[lens-1-i]:
                return False
        return True
