"""
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""

class ListNode:
def __init__(self, x):
    self.val = x
    self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        p1, p2, p3 = pHead, pHead, pHead
        while p1:
            if not p1 or not p2 or not p1.next or not p1.next.next:
                return None
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break
        while p1:
            if p1 == p3:    #一开始把这个判断写在下面了，应该写在开头。
                return p1          
            p1 = p1.next                
            p3 = p3.next
            
pNode1 = ListNode(1)
pNode2 = ListNode(2)
pNode3 = ListNode(3)
pNode4 = ListNode(4)

pNode1.next = pNode2
pNode2.next = pNode3
pNode3.next = pNode4
pNode4.next = pNode1

S = Solution()
print(S.EntryNodeOfLoop(pNode1))
