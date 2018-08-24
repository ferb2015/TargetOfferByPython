# 交换左右子结点，子节点下的子树也会搬到另一边的。 代码关键点1. return。并不是有return，递归时就要一定要将结果赋给某个变量。 2.self的使用，temp = TreeNode(0)。一开始用的temp = self.TreeNode(0)。错的。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root == None:
            return root
        if root.left or root.right: #这句话可有可无
            temp = TreeNode(0)  #这句话可有可无，注意self用法，不写成 self.TreeNode(0)/(None)
            temp = root.left
            root.left = root.right
            root.right = temp
        self.Mirror(root.left)  #注意 这里返回值，没有赋给某变量。直接执行语句。
        self.Mirror(root.right)
        return root
