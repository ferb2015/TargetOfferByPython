# 不能用递归啊，从上向下不好，要从下向上，知道两个初始值，慢慢推上去

class Solution:      
    def Fibonacci(self, n):
        # write code here
        f1=0
        f2=1
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            for i in range(n+1)[2:]:
                f = f1+f2
                f1 = f2
                f2 = f               
            return f
            
S = Solution()
p = S.Fibonacci(7)
print(p)

# 法二：

class Solution:      
    def Fibonacci(self, n):
        result = [0,1]
        a=n
        while n>=2:
            result.append(result[-1]+result[-2])    #不是result=result.append,就是result.append
            n=n-1
        return result[a]
            
S = Solution()
p = S.Fibonacci(8)
print(p)

# 或者： 
res = [0,1] while(len(res)<=n): res.append(res[-1]+res[-2]) return res[n]
