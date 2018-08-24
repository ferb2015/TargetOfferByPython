"""
这个很难想，一开始不知道要干什么，思路是如何复制一个链表，要新建结点，复制值、next指针、random指针。

分为三步完成：

一复制每个结点，并把新结点放在老结点后面，如1->2,复制为1->1->2->2

二为每个新结点设置other指针

三把复制后的结点链表拆开
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None    
        def clonenext(pHead):   #在def里又定义def，不能再加self了
            node = pHead
            while node:
                clone = RandomListNode(0)   #是一个结点 创建一个个结点
                clone.label = node.label
                clone.next = node.next
                node.next = clone
                node = clone.next
        
        def clonerandom(pHead):
            node = pHead
            while node:
                clone = node.next
                if node.random:
                    clone.random = node.random.next
                node = clone.next
                
        def separate(pHead):    #法一 自己写的
            node = pHead
            clone1 = node.next
            while node:
                clone = node.next
                if not clone.next:
                    node.next = None
                    clone.next = None
                    return clone1
                node.next = clone.next
                node = node.next
                clone.next = node.next        
        def ReconnectNodes(pHead):  #法二 剑指offer上的
            pNode = pHead
            pClonedHead = pClonedNode = pNode.next
            pNode.next = pClonedHead.next
            pNode = pNode.next
    
            while pNode:
                pClonedNode.next = pNode.next
                pClonedNode = pClonedNode.next
                pNode.next = pClonedNode.next
                pNode = pNode.next
    
            return pClonedHead        
        

        
        clonenext(pHead)
        clonerandom(pHead)
        return separate(pHead)
                    
node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.label)
