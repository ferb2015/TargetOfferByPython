
# 复杂度O(n)

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array,target):
        i,j=0,len(array)-1 #两指针 指向头和尾
        res = []
        while i<j:
            if array[i]+array[j]==target:
                res.append([array[i],array[j]])
                i += 1
                j -= 1
            if array[i]+array[j] > target:
                j -= 1
            if array[i]+array[j] < target:
                i +=1
        return res
