"""
题目描述
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""


# 这题看的别人的https://www.nowcoder.com/questionTerminal/6f8c901d091949a5837e24bb82a731f2

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        sign, decimal, hasE = False, False, False #正负号，小数，有没有E
        for i in range(len(s)):
            if s[i] == 'e' or s[i] == 'E' :
                if hasE:
                    return False
                if i == len(s)-1 :
                    return False
                hasE = True
            elif s[i] == '+' or s[i] =='-' :
                if sign and s[i-1]!='e' and s[i-1]!='E' :
                    return False
                if not sign and i>0 and s[i-1]!='e' and s[i-1]!='E' :
                    return False
                sign = True
            elif s[i] == '.' :
                if decimal or hasE:
                    return False
                decimal = True
            elif s[i] > '9' or s[i] < '0' :
                return False
        return True
