# 栈的问题，都一个一个入栈地分析，要想成初始栈里就有元素，从空栈，一个个压入开始分析。

# 辅助栈 概念。

# 错题集：1.self；2.self.min()忘记加(),函数记得加括号

class Solution:
    def __init__(self):
        self.stack = []
        self.assist = []
    def push(self, node):
        # write code here
        if not self.min() or node < self.min():     #之前写成self.min，忘记加()了
            self.assist.append(node)
        else:
            self.assist.append(self.min())      #或self.assist.append(self.assist[-1]不过不好
        self.stack.append(node)
    def pop(self):
        # write code here
        if self.stack:
            self.assist.pop()
            return self.stack.pop()
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
    def min(self):
        # write code here 
        if self.assist:
            return self.assist[-1]
