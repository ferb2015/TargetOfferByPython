# 字符串的全排列。
# 递归核心思想：可以写成诸如f(n) = f(n+*) ....的表达式

class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
         
        def Permutation(startIdx):
            if startIdx >= len(arrSs):
                clone = ''.join(arrSs)
                res.append(clone)
            else:
                changeIdx = startIdx
                while changeIdx < len(arrSs):
                    arrSs[changeIdx], arrSs[startIdx] = arrSs[startIdx], arrSs[changeIdx]
                    Permutation(startIdx + 1)
                    arrSs[changeIdx], arrSs[startIdx] = arrSs[startIdx], arrSs[changeIdx]
                    changeIdx += 1
         
        res = []
        arrSs = list(ss)
        Permutation(0)
        res = list(set(res))
        return sorted(res)
