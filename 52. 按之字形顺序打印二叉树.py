
"""
题目描述
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""
# 参考了 https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target Offer/按之字形顺序打印二叉树.py

# 是层次遍历的变形，我知道的，但还是没能写出来。每次打印一层，不要全部一起打印。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 存储点的时候按照奇数层和偶数层分别存储
    def Print(self, pRoot):
        if not pRoot:
            return []
        result, nodes = [], [pRoot]
        right = True
        while nodes:
            curStack, nextStack = [], []
            if right:
                for node in nodes:
                    curStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
            else:
                for node in nodes:
                    curStack.append(node.val)
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)
            nextStack.reverse()
            right = not right
            result.append(curStack)
            nodes = nextStack
        return result
    # 转换思路，存储的时候一直从左向右存储，打印的时候根据不同的层一次打印
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        level, result, lefttoright = [root], [], True
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
            lefttoright = not lefttoright
            if curres:
                result.append(curres)
            level = nextlevel
        return result


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
aList = S.zigzagLevelOrder(pNode1)
print(aList)
