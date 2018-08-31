"""
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 
数值为0或者字符串不是一个合法的数值则返回0。

输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0

示例1
输入:
+2147483647
    1a33
    
输出:
2147483647
    0
"""

# 要点在于如何把str转换成int型。 设置一个number = ['0','1','2','3','4','5','6','7','8','9'] 
# 然后number.index(i),比如i是 '1'，返回对应的下标1，这个是int型，很巧妙。

class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        if len(s)==1:   
            if s <= '0' or s >= '9':
                return 0
        lable = 1
        start = 0
        if s[0] == '+' :
            lable = 1
            start = 1
        if s[0] == '-':
            lable = -1
            start = 1
        summ = 0
        number = ['0','1','2','3','4','5','6','7','8','9']
        for i in s[start:]:
            if i <= '0' or i >= '9':
                return 0
            summ = summ*10 + number.index(i)
            
        return summ*lable
