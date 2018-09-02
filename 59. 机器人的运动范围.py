"""
题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""

# 回溯法。有了上一题“矩阵的路径”的经验，在上一题的基础上更改代码就行了。
# return还是遇到了问题，这里flag=1之后不用再flag=0，依然是看牛客网讨论区的回答才AC.

class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        flag = [0]*rows*cols
        count = [0]*rows*cols
        #或 flag = [[0 for col in range(cols)] for row in range(rows)] 下面用flag[i][j]
        def helper(threshold, rows, cols, i, j, flag, count):
            index = i * cols + j
            if i < 0 or i >= rows or j < 0 or j >= cols or \
                sum(list(map(int,str(i))))+sum(list(map(int,str(j)))) > threshold or \
                flag[index] == 1:
                return 0
            flag[index] = 1
            count[index] = 1
            helper(threshold,rows,cols, i - 1, j, flag,count)
            helper(threshold, rows, cols, i + 1, j, flag,count)
            helper(threshold, rows, cols, i, j - 1, flag,count)
            helper(threshold, rows, cols, i, j + 1, flag,count)
            return count 
        summ = helper(threshold, rows, cols, 0, 0, flag,count)
        if summ == 0:
            return 0
        else:
            return sum(summ)
            
            
# 参考牛客网上：

class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        flag = [0]*rows*cols
        #flag = [[0 for col in range(cols)] for row in range(rows)]
        def helper(threshold, rows, cols, i, j, flag):
            index = i * cols + j
            if i < 0 or i >= rows or j < 0 or j >= cols or \
                sum(list(map(int,str(i))))+sum(list(map(int,str(j)))) > threshold or \
                flag[index] == 1:
                return 0
            flag[index] = 1
            return helper(threshold,rows,cols, i - 1, j, flag)+ \
                helper(threshold, rows, cols, i + 1, j, flag)+ \
                helper(threshold, rows, cols, i, j - 1, flag)+ \
                helper(threshold, rows, cols, i, j + 1, flag) +1
        return helper(threshold, rows, cols, 0, 0, flag)
