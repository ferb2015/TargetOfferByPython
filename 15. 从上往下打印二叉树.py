# BFS广度优先搜索算法，用queue队列，这题我以为要用递归的方法，想的都是递归怎么做，原来可以通过迭代实现，那么，要怎么找完root，找left和right呢？答案是通过一个list，list放的每个元素是treenode，每次读一个，就能依次遍历了。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = []
        result = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
