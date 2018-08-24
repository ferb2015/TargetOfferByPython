# 这个题要好好理清楚，多刷几遍。 思路是肯定要用两个函数的，step1.遍历 找到是否有相同的第一个结点，step2.在有第一个相同结点的基础上，才跳进新函数，去分别遍历左子树和左子树匹配，右子树和右子树匹配。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.zishu(pRoot1,pRoot2)
            if result == False:
                result = self.HasSubtree(pRoot1.left,pRoot2)
            if result == False:
                result = self.HasSubtree(pRoot1.right,pRoot2)                
        return result
        
    def zishu(self,pRoot1,pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return (self.zishu(pRoot1.left,pRoot2.left) and self.zishu(pRoot1.right,pRoot2.right))
