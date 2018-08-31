"""
题目描述
输入两个链表，找出它们的第一个公共结点。
"""
# 链表问题，出发点1.长度；2.双指针

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1, p2 = pHead1, pHead2
        n1, n2 = pHead1, pHead2
        l1, l2 = 0, 0
        while p1:
            l1+=1
            p1 = p1.next
        while p2:
            l2+=1
            p2 = p2.next
        if l1>l2:
            s = l1-l2
            while s:
                s-=1
                n1 = n1.next
        else:
            s = l2 - l1
            while s:
                s -=1
                n2 = n2.next
        while n2:
            if n1 == n2:    
                return n1
            n1 = n1.next
            n2 = n2.next
        
Node1 = ListNode(0)
Node2 = ListNode(1)
Node3 = ListNode(2)
Node1.next = Node2
Node2.next = Node3

Node4 = ListNode(4)
Node5 = ListNode(1)

Node4.next = Node5
Node5.next = Node2

S = Solution()
print(S.FindFirstCommonNode(Node1,Node4).val)
