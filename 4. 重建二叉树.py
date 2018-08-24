# 根据根节点，区分左子树、右子树。再分别对中序遍历的左子树右子树做相同操作。前序遍历的位置每次后移一位。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None        
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:   # 并不是None，所以if pre == None or tin == None:这是错的
            return None
        root = TreeNode(pre.pop(0))  #每次弹出一个
        index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre,tin[:index])
        root.right = self.reConstructBinaryTree(pre,tin[index+1:])
        return root
S = Solution()
p = S.reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
print(p.val)

# 或者改成

root = TreeNode(pre[0])
index = tin.index(root.val)
root.left = self.reConstructBinaryTree(pre[1:index+1],tin[:index])
root.right = self.reConstructBinaryTree(pre[index+1:],tin[index+1:])

# 也是一样的，因为pre[1:]从1开始，重新进去迭代，就是下一个了。
