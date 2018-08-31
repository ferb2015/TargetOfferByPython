"""
题目描述
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""

# python要进行越界检查 & 0xFFFFFFFF

# 正负数检查 num1 if num1<=0x7FFFFFFF else ~(num1^0xFFFFFFFF)

class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            summ = num1 ^ num2
            carry = (num1 & num2)<<1
            num1 = summ & 0xFFFFFFFF
            num2 = carry & 0xFFFFFFFF
        return num1 if num1<=0x7FFFFFFF else ~(num1^0xFFFFFFFF)
