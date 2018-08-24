# 二维数组中的查找
# 从右上到左下 注意while中内容怎么写

class Solution:
# array 二维列表
    def Find(self,target, array):
        # write code here
        rows = len(array) - 1  #行数
        cols= len(array[0]) - 1 #列数
        i = rows
        j = 0
        while j<=cols and i>=0:     #这里是<=和>=，一开始没习惯这么写
            if target<array[i][j]:
                i -= 1
            elif target>array[i][j]:
                j += 1
            else:
                return True
        return False

  a = Solution()
  print(a.Find(3,[[1,2],[3,5]]))
