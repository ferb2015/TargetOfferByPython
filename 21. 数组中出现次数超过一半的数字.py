# 这题用python直接来了。

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        for i in numbers:
            if numbers.count(i)>len(numbers)/2:
                return i
        return 0
S = Solution()
print(S.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))
