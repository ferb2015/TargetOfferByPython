class Solution:
    def IsPopOrder(self, pushV, popV):
        stack, k = [], 0
        # write code here
        # 用一个辅助栈 保存pushV的元素，重要的是if判断，先判断pushV[i]和popV[k]是否相等
        #再判断stack栈顶元素是否和pop[k]相等，相等就pop，k++。
        for i in range(len(popV)):
            stack.append(pushV[i])
            if pushV[i]==popV[k]:
                while stack!=[] and stack[-1] == popV[k]:
                    stack.pop()
                    k = k+1
        if k==len(popV):
            return True
        return False
            
        
pushV = [1,2,3,4,5]
popV = [4,5,3,2,1]
a = Solution()
print(a.IsPopOrder(pushV,popV))
