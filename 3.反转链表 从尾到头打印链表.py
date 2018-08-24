# 1.用stack实现；2.用递归实现,python中，a=[1,2],a=a+[3],则a=[1,2,3]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
     
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next)+[listNode.val]
        
node1=ListNode(10)
node2=ListNode(11)
node3=ListNode(12)
node1.next=node2
node2.next=node3
a = Solution()
print(a.printListFromTailToHead(node1))
