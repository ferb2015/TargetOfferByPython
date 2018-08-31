"""
题目描述
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""

"""
参考http://www.cnblogs.com/qiaojushuang/p/7780445.html

对于1-9，10-99，100-999，每个n位数中包含1的个数公式为：

f(1) = 1

f(2) = 9 * f(1) + 10 ** 1

f(3) = 9 * f(2) + 10 ** 2

f(n) = 9 * f(n-1) + 10 ** (n-1)

n位数一共的1个数：

s(1) = f(1)
s(2) = 9*s(1)+ 10 ** 1 + s(1)
s(3) = 9*s(2)+ 10 ** 1 + s(2)
高位数：分两种： 1.最高位==1时，最高位为1时的次数（eg.12345）为：2346次（联想：10000-19999的次数为9999+1，因此12345的次数为2346） 2.最高位>1时，最高位为1 时的次数(eg.22345）为):10000次，因为包含了最高位为1时所有可能（当最高位为1时）。
"""

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 10:
            return 1 if n >= 1 else 0
        #判断最高位为1时，1的个数
        gaowei = int(str(n)[0])
        weishu = len(str(n))
        if gaowei == 1:
            high = n - (10**(weishu-1))* gaowei + 1 #这个加1别忘了
                #high1 = high
        else:
            high = 10**(len(str(n))-1)
            
        def fn(n):
            if n <= 0:
                return 0
            if n == 1:
                return 1
            current = 9 * fn(n-1) + 10 ** (n-1)
            return fn(n-1) + current    #这步很重要
        """        
        def sum1(n):   #记录f(n)的和    #我自己写的，错误的fn
            if n <= 0:
                return 0
            def fn(n): #   n :位数
                if n <= 0:
                    return 0
                if n == 1:
                    return 1
                if n > 1:
                    return fn(n-1)*9 + 10**(n-1)
            summ=0
            for i in range(n+1)[1:]:
                summ = summ + fn(i) 
        """
        low = fn(weishu-1) * gaowei
        return high+low+ self.NumberOf1Between1AndN_Solution(n - gaowei * 10 ** (weishu-1))   

        
S = Solution()
print(S.NumberOf1Between1AndN_Solution(13))
