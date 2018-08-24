# 这题还是没能自己做出来。是dfs搜索，用递归，但不知道怎么用。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        res = []
        if not root:
            return res
        path = [root]  #保存根节点
        sums = [root.val]
        def dfs(root):  #深度优先搜索的变形，不是用while，而是用递归！
            if root.left:
                path.append(root.left)
                sums.append(root.left.val+sums[-1])
                dfs(root.left)
            if root.right:
                path.append(root.right)
                sums.append(root.right.val+sums[-1])
                dfs(root.right)
            if not root.left and not root.right:
                if sums[-1] == expectNumber:
                    res.append([p.val for p in path])
            path.pop()
            sums.pop()
        dfs(root)
        return res       
    
pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5


S = Solution()
print(S.FindPath(pNode1, 22))
