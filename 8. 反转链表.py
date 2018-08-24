# 不要while pHead.next!=None:就用while pHead:

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        prev = None
        pcur = pHead
        while pcur:
            tmp = pcur.next    #暂存pcur.next
            pcur.next = prev    #反转
            prev = pcur    #移到下一位  # 不是prev.next = pcur   （.next想成一个指针 指向某处）移动的只有pcur。
            #或者想成prev是指针，只有指向的地址变了，它本身没有.next的概念的。
            pcur = tmp    #移到下一位
        return prev     #新表头 就是末尾
