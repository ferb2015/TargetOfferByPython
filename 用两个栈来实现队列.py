"""
入队：将元素进栈A

出队：判断栈B是否为空，如果为空，则将栈A中所有元素pop，并push进栈B，栈B出栈；

如果不为空，栈B直接出栈。
"""

class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
         
    def push(self, node):
        # write code here
        self.stackA.append(node)
         
    def pop(self):
        # return xx
        if self.stackB:
            return self.stackB.pop(0)
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop(0))  #可以写pop()或pop(0)
            return self.stackB.pop(0)
    
    
S = Solution()
S.push(7)
S.push(5)
S.push(4)
print(S.pop())
