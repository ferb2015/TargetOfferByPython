# 直接用python里的函数replace(old,new)。

# 法一
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        s = s.replace(' ','%20')
        return news
a = Solution()
print(a.replaceSpace("as d "))

#法二：
class Solution:
# s 源字符串
    def replaceSpace(self, s):
        news = ''
        for j in s:
            if j == ' ':
                news = news + '%20'
            else:
                news =  news + j
        return news
a = Solution()
print(a.replaceSpace("as d "))

