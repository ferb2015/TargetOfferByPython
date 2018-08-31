"""
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。
"""

# 这题和“字符串的排列”那题是一样的，都是全排列。 把数组变成一串数字：int(''.join([str(t) for t in arrSs]))

class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
         
        def Permutation(startIdx):
            if startIdx >= len(arrSs):
                clone = int(''.join([str(t) for t in arrSs]))
                res.append(clone)
            else:
                changeIdx = startIdx
                while changeIdx < len(arrSs):
                    arrSs[changeIdx], arrSs[startIdx] = arrSs[startIdx], arrSs[changeIdx]
                    Permutation(startIdx + 1)
                    arrSs[changeIdx], arrSs[startIdx] = arrSs[startIdx], arrSs[changeIdx]
                    changeIdx += 1
         
        res = []
        arrSs = numbers
        Permutation(0)
        res = list(set(res))
        return min(sorted(res))        
S = Solution()
print(S.PrintMinNumber([12,34,56]))


# 法二：拼接成的数组mn和nm比较，马上能得出大小（cmp的用法）。拼接用字符串拼接（数字转换成字符串）。

from functools import cmp_to_key

def cmp(a, b):
    return int(str(a)+str(b)) - int(str(b)+str(a))


def print_mini(nums):
    if not nums:
        return
    print (int(''.join([str(num) for num in sorted(nums, key=cmp_to_key(cmp))])))


if __name__ == '__main__':
    test = [3,32,321]
    print_mini(test)
