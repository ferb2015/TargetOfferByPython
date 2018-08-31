"""
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。
求按从小到大的顺序的第N个丑数。
"""
# 这题很巧妙。下次要再做一次才行。下面是看别人的答案

class Solution:
    def GetUglyNumber_Solution(self,n):
        if n <= 0:
            return 0
        ugly = [1]
        t2, t3, t5 = 0, 0, 0  # 分别标记乘以2，3，5的丑数索引
        while n > 1:
            while ugly[t2] * 2 <= ugly[-1]:
                t2 += 1
            while ugly[t3] * 3 <= ugly[-1]:
                t3 += 1
            while ugly[t5] * 5 <= ugly[-1]:
                t5 += 1
            ugly.append(min([ugly[t2]*2, ugly[t3]*3, ugly[t5]*5]))
            n -= 1
        return ugly[-1]
