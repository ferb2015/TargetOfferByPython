# 这个用python还是有点麻烦的,for循环range的使用。还有就是用res.append。这题看答案的，首先要设置top bottom left right。

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        rows = len(matrix)-1      #行
        cols = len(matrix[0])-1   #列
        left=0
        right=cols
        top=0
        bottom=rows
        res = []
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            for i in range(top+1,bottom+1): 
                res.append(matrix[i][right])
            if top!=bottom:                 #判断 上等于下的时候，就不需要从右到左再遍历了
                for i in range(right-1,left-1,-1):  #很复杂 从大到小 这里是left-1而不是left+1
                    res.append(matrix[bottom][i])
            if left!=right:                 #判断 左等于右的时候，就不需要从下到上再遍历了
                 for i in range(bottom-1,top,-1):   #右边取闭区间top+1，所以这里是top
                     res.append(matrix[i][left])
            left=left+1
            right = right-1
            top = top+1
            bottom = bottom-1
        return res
    
a = Solution()
matrix = [[1,2,3],[4,5,6]]
print(a.printMatrix(matrix))
