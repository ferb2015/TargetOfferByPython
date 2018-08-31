用list存每个结点

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree): #中序遍历 right:前向链表 left：后向链表
        # write code here
        if not pRootOfTree: #一开始没写
            return
        a, b = [], []                
        def zhongxu(root):
            if not root:
                return 
            if pRootOfTree.left:
                zhongxu(root.left)
            a.append(root)   #访问根结点
            if root.right:
                zhongxu(root.right)
                
        zhongxu(pRootOfTree)
        for i in range(len(a))[:-1]:
            a[i].right = a[i+1]
        for i in range(len(a))[1:]:
            a[i].left = a[i-1]
        return a[0] #返回是a[0],而不是返回a
    
    #法二：l

    for i,v in enumerate(self.arr[:-1]):
        v.right = self.arr[i + 1]
        self.arr[i + 1].left = v
    return self.arr[0]
        
node1 = TreeNode(7)
node2 = TreeNode(5)
node3 = TreeNode(8)
node4 = TreeNode(4)
node5 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5


S = Solution()
print(S.Convert(node1))
