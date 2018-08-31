"""
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
"""

# 这题有两种解法，一种是我们熟知的动态规划算法，还有一种挺巧妙的，看的剑指 offer里的。

# 法一：

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        a = False
        if not array:
            a = True
            return 0
        a = False
        cur = 0
        Sum = -1000
        for i in array:
            if cur <= 0:    #cur<=0 说明前面累加的白加了，可以从下一个重新加起
                cur = i
            else:
                cur = cur + i
            if cur > Sum:
                Sum = cur
        return Sum
            
S = Solution()
print(S.FindGreatestSumOfSubArray([-3,5,-2]))

# 法二：动态规划！！！！！！一定要会啊
"""
f[i]表示以i结尾的子数组的最大和，只需求出max(f[i]),递归公式：

f[i] = array[i]             ( f[i-1]<=0 )   #前面累加小于0，所以不要前面的了，只保留最后这个
f[i] = array[i] + f[i-1]    ( f[i-1>0] )
"""
# 解法：

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        f = [None]*len(array)   #不能写f = np.zeros(len(array),在开头import numpy as np,牛客网不支持import numpy
        f[0] = array[0]
        for i in range(len(array))[1:]:
            if f[i-1]<=0:
                f[i] = array[i]
            else:
                f[i] = array[i] + f[i-1]
        return max(f)
